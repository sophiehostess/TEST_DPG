# https://blog.csdn.net/qq_42566199/article/details/108667368
# https://blog.csdn.net/qq_42566199/article/details/108709442
# https://www.jianshu.com/p/36e527888c5f
# https://github.com/hoffstadt/DearPyGui
# https://zhuanlan.zhihu.com/p/262853190
# https://blog.csdn.net/toseekin/article/details/109102654

# import sys
# import os

from dearpygui.core import *

def button_callback(sender, data):
    print(sender)
    print(data)

add_window("Window1")
add_button("Apply", callback=button_callback, callback_data="Hello World!")
add_button("Submit Data")
set_item_callback("Submit Data", callback=button_callback, callback_data="Hello World!")


add_window("Window2")
add_button("Apply", callback=button_callback, callback_data="Hello World!")
add_button("Submit Data")
set_item_callback("Submit Data", callback=button_callback, callback_data="Hello World!")



start_dearpygui()