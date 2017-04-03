#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime

def log(msg):
    curtime = str(datetime.datetime.now().time())
    print(msg)
    log_file_path = "log.txt"
    log_file = open(log_file_path,'a')
    log_file.write("\n%s: %s" % (msg,curtime))
    log_file.close()
