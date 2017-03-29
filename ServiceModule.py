#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import thread,os,sys
import Common
 
class RunService:
    def __init__(self):
        self.logger = Common.getLogger('RunService')
        thread.start_new(self.do_something, tuple())
        while True:
            if getattr(sys,'stopservice', False):
                break
                #sys.exit()
            time.sleep(0.3)
    
    def do_something(self):
        '''
        Do something
        '''
        while True:
            f = open(os.path.join(Common.DIR_PATH, 'test.txt') , 'a')
            f.write("current local time: %d-%d-%d %d:%d:%d\n" % time.localtime()[:6])
            f.close()
            self.logger.info("xxxxxxxxxxxx: %d-%d-%d %d:%d:%d" % time.localtime()[:6])
            time.sleep(3)
                
if __name__ == "__main__":
    RunService()
 