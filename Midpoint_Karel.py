#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  5 16:11:59 2025

@author: anyuchen
"""

from karel.stanfordkarel import *
#填滿除了最外側兩顆的beeper
#從左右慢慢一顆一顆拿，拿到最後一顆就是中心點

#180degree
def turn_around():
    turn_left()
    turn_left()

#fillrow without outer
def fill_row():
    move()
    while front_is_clear():
        put_beeper()
        move()

#move to end of beeper
def move_to_beeper():
    while beepers_present():
        move()

#pick left & right
def pick_outer():
    #先拿右邊
    move_to_beeper()
    turn_around()
    move()
    pick_beeper()
    move()

def main():
    #step1:fill a row
    fill_row()
    turn_around()
    move()
    #step2:拿兩端的beeper,基數跟偶數行會有不同面向，要設條件分開
    while beepers_present():
        pick_outer()
    if facing_east():
        turn_around()
        move()
        turn_around()
    else:
        turn_around()
    #step3:在中間點放beeper
    put_beeper()

# 執行主程式
if __name__ == '__main__':
    main()