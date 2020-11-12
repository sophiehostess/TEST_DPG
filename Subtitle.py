#coding=utf-8

from dearpygui.core import *
from dearpygui.simple import *

# set_global_font_scale(scale=1.5)

add_additional_font(file='C:\\WINDOWS\\FONTS\\ARIAL.TTF', size=20)


def _call_back_fun(sender, data):
    print(sender)
    print(data)


def _show_on_fun(sender, data):
    show_item('This is ON')
    show_item('Text Box 1##inputtext1')

def _show_off_fun(sender, data):
    hide_item('This is ON')
    hide_item('Text Box 1##inputtext1')


with window('main_window', no_title_bar=True, autosize=False):
    set_main_window_title("Realtime Subtitle")
    set_main_window_size(550, 650)
    set_main_window_resizable(False)
    add_input_text('Text Box 1##inputtext1', hint='please enter something here', on_enter=True, callback=_call_back_fun, tip='this is hints')
    add_button('show on', callback=_show_on_fun)
    add_button('show off', callback=_show_off_fun)
    add_text('This is ON', color=[0, 200, 200], parent='main_window')
    hide_item('This is ON')
    with menu_bar('menu bar'):
        with menu('menu 1'):
            add_menu_item('menu item')
        with menu('menu 2'):
            add_menu_item('menu item 2')



start_dearpygui(primary_window="main_window")