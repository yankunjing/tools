#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author CoderYkj
@desc Windows CMD命令行颜色
@date 2018/11/20
说明：
字体颜色定义，关键在于颜色编码，由2位十六进制组成，分别取0~f，前一位指的是背景色，后一位指的是字体色
由于该函数的限制，应该是只有这16种，可以前景色与背景色组合。也可以几种颜色通过或运算组合，组合后还是在这16种颜色中
"""

import ctypes

# 前景色
FOREGROUND_BLACK        = 0x00 # black
FOREGROUND_DARKBLUE     = 0x01 # dark blue
FOREGROUND_DARKGREEN    = 0x02 # dark green
FOREGROUND_DARKSKYBLUE  = 0x03 # dark skyblue
FOREGROUND_DARKRED      = 0x04 # dark red
FOREGROUND_DARKPINK     = 0x05 # dark pink
FOREGROUND_DARKYELLOW   = 0x06 # dark yellow
FOREGROUND_DARKWHITE    = 0x07 # dark white
FOREGROUND_DARKGRAY     = 0x08 # dark gray
FOREGROUND_BLUE         = 0x09 # blue
FOREGROUND_GREEN        = 0x0a # green
FOREGROUND_SKYBLUE      = 0x0b # skyblue
FOREGROUND_RED          = 0x0c # red
FOREGROUND_PINK         = 0x0d # pink
FOREGROUND_YELLOW       = 0x0e # yellow
FOREGROUND_WHITE        = 0x0f # white

# 背景色
BACKGROUND_BLUE         = 0x10 # dark blue
BACKGROUND_GREEN        = 0x20 # dark green
BACKGROUND_DARKSKYBLUE  = 0x30 # dark skyblue
BACKGROUND_DARKRED      = 0x40 # dark red
BACKGROUND_DARKPINK     = 0x50 # dark pink
BACKGROUND_DARKYELLOW   = 0x60 # dark yellow
BACKGROUND_DARKWHITE    = 0x70 # dark white
BACKGROUND_DARKGRAY     = 0x80 # dark gray
BACKGROUND_BLUE         = 0x90 # blue
BACKGROUND_GREEN        = 0xa0 # green
BACKGROUND_SKYBLUE      = 0xb0 # skyblue
BACKGROUND_RED          = 0xc0 # red
BACKGROUND_PINK         = 0xd0 # pink
BACKGROUND_YELLOW       = 0xe0 # yellow
BACKGROUND_WHITE        = 0xf0 # white

# 句柄号
STD_INPUT_HANDLE  = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE  = -12

# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

# 设置控制台颜色
def set_cmd_color (color, handle = std_out_handle):
    return ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)

# 重置控制台颜色
def reset_cmd_color ():
    set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

if __name__ == '__main__':
    import sys

    # dark blue 暗蓝色
    set_cmd_color(FOREGROUND_DARKBLUE)
    sys.stdout.write(u"FOREGROUND_DARKBLUE: 暗蓝色文字\n")
    reset_cmd_color()

    # dark green 暗绿色
    set_cmd_color(FOREGROUND_DARKGREEN)
    sys.stdout.write(u"FOREGROUND_DARKGREEN: 暗绿色文字\n")
    reset_cmd_color()

    # dark sky blue 暗天蓝色
    set_cmd_color(FOREGROUND_DARKSKYBLUE)
    sys.stdout.write(u"FOREGROUND_DARKSKYBLUE: 暗天蓝色文字\n")
    reset_cmd_color()

    # dark red 暗红色
    set_cmd_color(FOREGROUND_DARKRED)
    sys.stdout.write(u"FOREGROUND_DARKRED: 暗红色文字\n")
    reset_cmd_color()

    # dark yellow 暗黄色
    set_cmd_color(FOREGROUND_DARKYELLOW)
    sys.stdout.write(u"FOREGROUND_DARKYELLOW: 暗黄色文字\n")
    reset_cmd_color()

    # dark white 暗白色
    set_cmd_color(FOREGROUND_DARKWHITE)
    sys.stdout.write(u"FOREGROUND_DARKWHITE: 暗白色文字\n")
    reset_cmd_color()

    # dark gray 暗灰色
    set_cmd_color(FOREGROUND_DARKGRAY)
    sys.stdout.write(u"FOREGROUND_DARKGRAY: 暗灰色文字\n")
    reset_cmd_color()

    # blue 蓝色
    set_cmd_color(FOREGROUND_BLUE)
    sys.stdout.write(u"FOREGROUND_BLUE: 蓝色文字\n")
    reset_cmd_color()

    # green 绿色
    set_cmd_color(FOREGROUND_GREEN)
    sys.stdout.write(u"FOREGROUND_GREEN: 绿色文字\n")
    reset_cmd_color()

    # sky blue 天蓝色
    set_cmd_color(FOREGROUND_SKYBLUE)
    sys.stdout.write(u"FOREGROUND_SKYBLUE: 天蓝色文字\n")
    reset_cmd_color()

    # red 红色
    set_cmd_color(FOREGROUND_RED)
    sys.stdout.write(u"FOREGROUND_RED: 红色文字\n")
    reset_cmd_color()

    # pink 粉红色
    set_cmd_color(FOREGROUND_PINK)
    sys.stdout.write(u"FOREGROUND_PINK: 粉红色文字\n")
    reset_cmd_color()

    # yellow 黄色
    set_cmd_color(FOREGROUND_YELLOW)
    sys.stdout.write(u"FOREGROUND_YELLOW: 黄色文字\n")
    reset_cmd_color()

    # white 白色
    set_cmd_color(FOREGROUND_WHITE)
    sys.stdout.write(u"FOREGROUND_WHITE: 白色文字\n")
    reset_cmd_color()

    # white bkground and black text 白底黑字
    set_cmd_color(FOREGROUND_BLACK | BACKGROUND_WHITE)
    sys.stdout.write(u"FOREGROUND_BLACK | BACKGROUND_WHITE: 白底黑字输出\n")
    reset_cmd_color()

    # white bkground and black text 黄底蓝字
    set_cmd_color(BACKGROUND_YELLOW | FOREGROUND_RED)
    sys.stdout.write(u"BACKGROUND_YELLOW | FOREGROUND_RED: 黄底蓝字输出\n")
    reset_cmd_color()

    # white bkground and black text 白底黑字2
    set_cmd_color(0xf0)
    sys.stdout.write(u"0xf0: 白底黑字输出2\n")
    reset_cmd_color()
