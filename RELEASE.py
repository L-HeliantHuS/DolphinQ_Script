#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ Author: HeliantHuS
@ Codes are far away from bugs with the animal protecting
@ Time:  4/4/2020
@ FileName: 海豚暂停与恢复.py
"""
import psutil
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    ProcessName = "DolphinQ.exe"
    PID = -1

    for i in psutil.process_iter():
        if i.name() == ProcessName:
            PID = i.pid

    dolphinQ = psutil.Process(PID)

    dolphinQ.resume()

else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:#in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", str(sys.executable), str(__file__), None, 1)