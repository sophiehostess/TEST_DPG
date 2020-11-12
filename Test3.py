from dearpygui.core import *

add_window("Tutorial")
add_text("This is some text on window 1")
end()

from dearpygui.simple import *

with window("Tutorial##2"):
    add_text("This is some text on window 2")

start_dearpygui()