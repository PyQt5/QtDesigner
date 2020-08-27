#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2020年2月2日
@author: Irony
@site: https://pyqt.site , https://github.com/892768447
@email: 892768447@qq.com
@file: __init__
@description: Qt Designer
'''

import os
import sys
from subprocess import Popen, run

__all__ = ['assistant', 'designer', 'linguist', 'qmlview']

CurrentDir = os.path.dirname(__file__)


def assistant():
    os.chdir(CurrentDir)
    if len(sys.argv) == 0:
        sys.argv.insert(0, os.path.join(CurrentDir, 'assistant.exe'))
    else:
        sys.argv[0] = os.path.join(CurrentDir, 'assistant.exe')
    Popen(sys.argv)


def designer():
    os.chdir(CurrentDir)
    if len(sys.argv) == 0:
        sys.argv.insert(0, os.path.join(CurrentDir, 'designer.exe'))
    else:
        sys.argv[0] = os.path.join(CurrentDir, 'designer.exe')
    Popen(sys.argv)


def linguist():
    os.chdir(CurrentDir)
    if len(sys.argv) == 0:
        sys.argv.insert(0, os.path.join(CurrentDir, 'linguist.exe'))
    else:
        sys.argv[0] = os.path.join(CurrentDir, 'linguist.exe')
    Popen(sys.argv)


def qmlview():
    os.chdir(CurrentDir)
    if len(sys.argv) == 0:
        sys.argv.insert(0, os.path.join(CurrentDir, 'qml.exe'))
    else:
        sys.argv[0] = os.path.join(CurrentDir, 'qml.exe')
    run(sys.argv)


if __name__ == "__main__":
    assistant()
    designer()
    linguist()
    qmlview()
