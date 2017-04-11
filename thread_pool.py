# -*- encoding:utf-8 -*-
"""
simple thread pool
"""

import Queue
import logging
import threading
import time
import traceback
import time_util

class ThreadPool(object):
    """
    thread_pool
    """

    def __init__(self, thread_num, task_size=500, thread_alive_time=300):
        """
        init thread pool
        Args: thread_num: thread in pool number
        Args: thread_alive_time: thread alive time
        """
        self.thread_alive_time = thread_alive_time
        self.task_queue = Queue.Queue(task_size)
        self.thread_list = list()

        # 预留2线程
        self.safe_thread_num = 2
        self.thread_num = thread_num

        self._stop = False
        self._lock = threading.Lock()

    def add_task(self, call_func, *func_args):
        """
        add task, put task into task queue
        Args:
            call_func: task's call_function
            func_args: callback function args
        """
        logging.debug("add one task")
        logging.debug("add task queue size[%s]" % self.task_queue.qsize())
        self.task_queue.put((call_func, func_args))

    def stop(self):
        """
        stop do task
        """
        self._stop = True

    def start(self):
        """
        start do task
        """
        main_thread = threading.Thread(target=self._main_start)
        main_thread.setDaemon(True)
        main_thread.start()

    def _main_start(self):
        """
        start do work, if no free thread the method will block
        Return: free thread
        """
        self._stop = False

        # semaphore = threading.Semaphore(self.thread_num)
        while not self._stop:

            # self._lock.acquire()
            thread = self._get_free_thread()

            if thread is not None:
                logging.debug("thread[%s] will do next task!" % thread.getName())

                task = self.task_queue.get(block=True)

                thread.do_func(task[0], *task[1])

                self.task_queue.task_done()
            else:
                # no free thread, sleep 1s
                time.sleep(1)

            # self._lock.release()

        for thread in self.thread_list:
            thread.join()

    def _get_free_thread(self):
        for thread in self.thread_list:
            logging.debug("thread[%s] alive [%s]" % (thread.getName(), thread.isAlive()))
            if not thread.isAlive():
                self.thread_list.remove(thread)

        for thread in self.thread_list:
            logging.debug("thread[%s] is_overtime[%s] is_free[%s]" % (thread.getName,
                                                                      thread.is_overtime(),
                                                                      thread.is_free()))
            if not thread.is_overtime() and thread.is_free():
                return thread

        if len(self.thread_list) < self.thread_num + self.safe_thread_num:
            thread = TaskWorkThread(self.thread_alive_time)
            thread.setDaemon(True)
            thread.start()
            self.thread_list.append(thread)

            return thread

        return None


class TaskWorkThread(threading.Thread):
    """
    execute thread
    """

    def __init__(self, alive_time):
        """
        Args: alive_time: thread alive time
        """
        threading.Thread.__init__(self)
        self.work_is_free = True
        self.callback_func = None
        self.func_args = None
        self.thread_is_overtime = False

        self.timer = time_util.Timer(alive_time)

        # self.semaphore = None

    def run(self):
        """
        execute callback function
        if thread is overtime, end
        """
        while not self.thread_is_overtime:
            if self.work_is_free:
                logging.debug("now thread [%s] is free, runtime[%s]"
                              % (self.getName(), self.timer.runtime()))
                self.thread_is_overtime = self.timer.is_overtime()
                time.sleep(2)
            else:
                logging.debug("thread[%s] start do function")
                try:
                    if len(self.func_args) == 0:
                        self.callback_func()
                    else:
                        self.callback_func(*self.func_args)

                    logging.debug("thread[%s] end do function")
                except Exception as e:
                    logging.warning('callback func raise error.[error=%s]'
                                    % traceback.format_exc())
                finally:
                    self.timer.update_start()
                    self.work_is_free = True

        logging.info("thread[%s] is run over" % self.getName())

    def do_func(self, callback_func, *func_args):
        """
        set thread execute function
        Args:
            callback_func: callback function
            func_args: function args
        """
        logging.debug("thread[%s] do function [%s]" % (self.getName(), callback_func))
        self.callback_func = callback_func
        self.func_args = func_args
        self.work_is_free = False

    def is_overtime(self):
        """
        Return: return the thread isn't overtime
        """
        return self.thread_is_overtime

    def is_free(self):
        """
        Return: return the thread isn't free
        """
        return self.work_is_free

class Timer(object):
    """
    timer
    计时器
    """

    def __init__(self, timeout=0):
        """
        Args:
            timeout: second, if second less than 0, will never timeout
        """
        self.start_time = time.time()
        self.timeout = timeout

    def update_start(self):
        """
        update timer start time
        """
        self.start_time = time.time()

    def is_overtime(self):
        """
        computer time is overtime
        Return: isn't overtime
        """
        if self.timeout <= 0:
            return False

        if time.time() - self.start_time > self.timeout:
            return True

        return False

    def runtime(self):
        """
        Returns: run second
        """
        return time.time() - self.start_time

