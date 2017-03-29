#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
buildservice = True
if '--no-service' in sys.argv[1:]:
    buildservice = False
    sys.argv = [k for k in sys.argv if k != '--no-service']
    print sys.argv
        
from distutils.core import setup
import os
import py2exe
import glob
import shutil
 
sys.path.insert(0,os.getcwd())

DESCRIPTION = 'Servicio de pruebas'
NAME = 'servicetest'

#includes = ["encodings", "encodings.*"]
OPTIONS = {"py2exe":
    {"compressed": 1, #压缩
    "optimize": 2,
    "ascii": 1,
    "packages": "encodings",
    "includes": "win32com,win32service,win32serviceutil,win32event",
    "dll_excludes": ["msvcp90.dll"],
    "bundle_files": 1 #所有文件打包成一个exe文件 
    }
}

if not buildservice:
    print 'Compile executable to windows...'
    setup(
        name = NAME ,
        description = DESCRIPTION,
        version = '0.1.0.0',
        console = ['ServiceModule.py'],
        zipfile=None,
        options = OPTIONS,
    )
else:
    print 'Compile services to windows...'
    setup(
        name = NAME,
        description = DESCRIPTION,
        version = '0.1.0.0',
        service = [{'modules':["ServiceLauncher"], 'cmdline':'pywin32'}],
        zipfile = None,
        options = OPTIONS,
    )
 
