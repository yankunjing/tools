#!/usr/bin/python3
# -*- coding: utf-8 -*-

def char_to_value (char):
    if char == '.':
        return  0

    if ord(char) >= ord('1') and ord(char) <= ord('5'):
        return (ord(char) - ord('1')) + 1

    if ord(char) >= ord('a') and ord(char) <= ord('z'):
        return (ord(char) - ord('a')) + 6

    return 0

def to_number (str):
    if len(str) > 13:
        assert(False, "string is too long to be a valid name")

    count = min(len(str), 12)

    value = 0
    for i in range(count):
        value = value << 5
        value = value | char_to_value(str[i])

    value = value << (4 + 5 * (12 - count))

    if len(str) == 13:
        v = char_to_value(str[12])
        if v > 0x0F:
            assert(False, "thirteenth character in name cannot be a letter that comes after j")
        value |= v

    return value
