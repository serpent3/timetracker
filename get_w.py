#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_w():
    def get_w_loop():
        sleep(2)
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
        this_w = 35076598

    while True:
        print('Нужно 5 секунд продержать курсор в окне, которое отслеживать')
        f = get_w_loop()
        sleep(2)
        s = get_w_loop()
        sleep(1)
        t = get_w_loop()
        if f != s or s != t:
            print('Ещё раз')
        else:
            return t
        
this_w = get_w()
print(this_w)
with open('this_w', 'w') as f:
    f.write(str(this_w))