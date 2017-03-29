#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys, logging

def we_are_frozen():
    """Returns whether we are frozen via py2exe.
    This will affect how we find out where we are located."""

    return hasattr(sys, "frozen")

def module_path():
    """ This will get us the program's directory,
    even if we are frozen using py2exe"""

    if we_are_frozen():
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)

VERSION = "2.0.6"
DIR_PATH = module_path()
DEF_CONF_FILE = os.path.join(DIR_PATH, 'setting.conf')

def loadSetting(path = DEF_CONF_FILE):
    config = {}
	# read config file
    try:
        fp = open(path, "r")
    except IOError:
        # use default parameters
        return config
    # parse user defined parameters
    while True:
        line = fp.readline()
        if line == "":
            # end line
            break
        line = line.strip()
        if line == "":
            continue
        if line.startswith("#"):
            continue
        (name, sep, value) = line.partition("=")
        if sep == "=":
            name = name.strip().lower()
            value = value.strip()
            config.update({name:value})
    fp.close()
    return config

def getLogger(loggerName):
    logger = logging.getLogger(loggerName)
    #import inspect
    #this_file = inspect.getfile(inspect.currentframe())
    #dirpath = os.path.abspath(os.path.dirname(this_file)) # "c:\windows\system32\" same as os.getcwd()
    handler = logging.FileHandler(os.path.join(DIR_PATH, loggerName + ".log"))
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    
    return logger
                
if __name__ == "__main__":
    pass
    # empty
 