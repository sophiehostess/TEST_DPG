from dearpygui.core import *
from dearpygui.simple import *




with window("Tutorial"):
    add_checkbox("Radio Button", default_value=False)
    print("单选按钮的值为: ", get_value("Radio Button"))
    set_value("Radio Button", True)
    print("设置新值后，单选按钮的值为: ", get_value("Radio Button"))


# 可以通过使用 start_dearpygui 方法的 primary_window 参数或使用 set_primary_window 方法将一个窗口设置为主窗口。
start_dearpygui(primary_window="Tutorial")