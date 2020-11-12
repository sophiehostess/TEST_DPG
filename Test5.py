from dearpygui.core import *
from dearpygui.simple import *

add_additional_font(file='C:\\WINDOWS\\FONTS\\ARIAL.TTF', size=20)
with window("Tutorial"):
    set_main_window_size(400, 400)

    add_text('DearPyGUI Generated This Text')

    add_text('Below You Will See two buttons')

    add_button("Button 1")

    add_same_line(spacing=30) #Adding a space on the same line

    add_button("Button 2")

# start_dearpygui()
start_dearpygui(primary_window="Tutorial")