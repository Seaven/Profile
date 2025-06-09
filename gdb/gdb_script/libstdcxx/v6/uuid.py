import gdb
import uuid

class DorisUuid(gdb.Command):
    def __init__(self):
        super(self.__class__, self).__init__("uuid", gdb.COMMAND_USER)

    def invoke(self, args, from_tty):
        argv = gdb.string_to_argv(args)
        hi = gdb.parse_and_eval(argv[0])
        lo = gdb.parse_and_eval(argv[1]) 
        hi = int(hi)
        lo = int(lo)

        if hi < 0: hi =(1 <<64) + hi
        if lo < 0: lo = (1 << 64) + lo
        value = (hi << 64) + lo
        x = uuid.UUID(int = value)
        gdb.execute('print "' + str(x) + '"')

DorisUuid()
