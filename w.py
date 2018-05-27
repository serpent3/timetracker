#! /usr/bin/env python3
import sys
from ctypes import *
import time

from conf import interval, log

# https://unix.stackexchange.com/questions/16131
# /how-do-i-find-the-x-window-id-under-the-mouse-pointer-in-bash
def w():    
    Xlib = CDLL("libX11.so.6")
    display = Xlib.XOpenDisplay(None)
    if display == 0: sys.exit(2)
    w = Xlib.XRootWindow(display, c_int(0))
    (root_id, child_id) = (c_uint32(), c_uint32())
    (root_x, root_y, win_x, win_y) = (c_int(), c_int(), c_int(), c_int())
    mask = c_uint()
    ret = Xlib.XQueryPointer(display, c_uint32(w), byref(root_id), byref(child_id),
                             byref(root_x), byref(root_y),
                             byref(win_x), byref(win_y), byref(mask))
    if ret == 0: sys.exit(1)
    Xlib.XCloseDisplay(display);
    return child_id.value 

with open ('this_w', 'r') as f:
    this_w = f.readline()#35076598 #w() # get windows
#this_w = 35076598
    
while True:
    time.sleep(interval)
    now_w = w()
    print (now_w)  
    if now_w == this_w:
        with open(log, 'a') as q:
            q.write('{}\n'.format(time.time()))