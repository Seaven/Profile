import re
import gdb

def print_ptr(ptr):
    # input param name
    col = gdb.parse_and_eval(ptr)
    col_print = gdb.execute('print %s' % ptr, to_string=True)
    re_out = re.search(r'(\$\d+? = )(.+)', col_print)

    #gdb.execute('print "xx: %s"' % re_out)
    if re_out:
        col_out = re_out.group(2)
    #    gdb.execute('print "xx1: %s"' % col_out)
    else:
        return

    is_raw_ptr = re.search(r'^\((.+?) \*.*?\) (0x.+)$', col_out)
    is_unique_ptr = re.search(r'^std::unique_ptr<(.+?)> = {get\(\) = (0x.+)}$', col_out)
    is_shared_ptr = re.search(r'^std::shared_ptr<(.+?)> .+? {get\(\) = (0x.+)}$', col_out) 

    #gdb.execute('print "type : %s"' % col.type.name)
    #gdb.execute('print "dynamic_type : %s"' % col.dynamic_type.name)
    #gdb.execute('print "unique: %s, share: %s, raw: %s"' % (is_unique_ptr, is_shared_ptr, is_raw_ptr))

    clazz = None
    col_ptr = None
    if is_unique_ptr:
        #gdb.execute('print "unique : %s, %s"' % (is_unique_ptr.group(1), is_unique_ptr.group(2)))
        clazz = is_unique_ptr.group(1)
        col_ptr = is_unique_ptr.group(2)
        #gdb.execute('print *((%s*) %s)' % (is_unique_ptr.group(1), is_unique_ptr.group(2)))
    elif is_shared_ptr:
        #gdb.execute('print "shared : %s, %s"' % (is_shared_ptr.group(1), is_shared_ptr.group(2)))
        clazz = is_shared_ptr.group(1)
        col_ptr = is_shared_ptr.group(2)
        #gdb.execute('print *((%s*) %s)' % (is_shared_ptr.group(1), is_shared_ptr.group(2)))
    elif is_raw_ptr:
        clazz = is_raw_ptr.group(1)
        col_ptr = is_raw_ptr.group(2)
        #gdb.execute('print *((%s*) %s)' % (is_raw_ptr.group(1), is_raw_ptr.group(2)))
    else:
        return 

    real_col = gdb.parse_and_eval("*((%s*) %s)" % (clazz, col_ptr))
    gdb.execute('print *((%s*) %s)' % (real_col.dynamic_type, col_ptr))

class Pcol(gdb.Command):
    def __init__(self):
        super(self.__class__, self).__init__("pcol", gdb.COMMAND_USER)

    def invoke(self, args, from_tty):
        argv = gdb.string_to_argv(args)
        ptr = argv[0]

        clazz = None
        try:
            gdb.lookup_type("starrocks::Column")
            clazz = "starrocks::Column"
        except Exception as e:
            gdb.lookup_type("starrocks::vectorized::Column")
            clazz = "starrocks::vectorized::Column"


        if ptr.startswith('0x'):
            col = gdb.parse_and_eval("*((%s*) %s)" % (clazz, ptr))
            gdb.execute('print *((%s*) %s)' % (col.dynamic_type, ptr))
            return

        print_ptr(ptr)

Pcol()


class Ptr(gdb.Command):
    def __init__ (self):
        super(self.__class__, self).__init__("ptr", gdb.COMMAND_USER)

    def invoke(self, args, from_tty):
        argv = gdb.string_to_argv(args)

        if len(argv) == 1:
            ptr = argv[0]
            gdb.execute('print %s' % ptr)
            print_ptr(ptr)
        elif len(argv) == 2:
            clazz = argv[0]
            ptr = argv[1]
            col = gdb.parse_and_eval("*((%s*) %s)" % (clazz, ptr))
            gdb.execute('print *((%s*) %s)' % (col.dynamic_type, ptr))

Ptr()

