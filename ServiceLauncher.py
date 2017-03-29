#!/usr/bin/python
# -*- coding: utf-8 -*-

import win32serviceutil
import win32service
import win32event
import win32evtlogutil
import os
import sys
import time

sys.stopservice = False

class ServiceLauncher(win32serviceutil.ServiceFramework):
    """
    Usage: 'ServiceLauncher.py [options] install|update|remove|start [...]|stop|restart [...]|debug [...]'
    Options for 'install' and 'update' commands only:
     --username domain\username : The Username the service is to run under
     --password password : The password for the username
     --startup [manual|auto|disabled|delayed] : How the service starts, default = manual
     --interactive : Allow the service to interact with the desktop.
     --perfmonini file: .ini file to use for registering performance monitor data
     --perfmondll file: .dll file to use when querying the service for
       performance data, default = perfmondata.dll
    Options for 'start' and 'stop' commands only:
     --wait seconds: Wait for the service to actually start or stop.
                     If you specify --wait with the 'stop' option, the service
                     and all dependent services will be stopped, each waiting
                     the specified period.
    """

    #服务名
    _svc_name_ = 'ServiceTest'
    #服务显示名称
    _svc_display_name_ = "Python Service Demo"
    #服务描述
    _svc_description_ = "Python service demo Description."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        import Common
        self.logger = Common.getLogger(self._svc_name_)

    def SvcStop(self):
        self.logger.info(self._svc_name_ + " do stop....")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        sys.stopservice = True
        win32event.SetEvent(self.hWaitStop)

        # ??? here ???
        #win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

    def SvcDoRun(self):
        self.logger.info(self._svc_name_ + " do run....") 
        sys.path.insert(0, os.getcwd())
        import ServiceModule
        ServiceModule.RunService()