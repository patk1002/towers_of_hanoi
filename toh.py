#! /usr/bin/env python3

"""
Recursive Python3 Towers of Hanoi
https://stackoverflow.com/questions/25118520/pythons-argparse-how-to-use-keyword-as-arguments-name

"""

import argparse
import sys

moveCount = 0

def move(f, t) :
    global moveCount
    print(f'Move disc from {f} to {t}.')
    moveCount += 1

def moveVia(f, v, t) :
    move(f, v)
    move(v, t)

def hanoi(n, f, h, t) :
    if n>0 :
        hanoi(n-1, f, t, h)
        move(f, t)
        hanoi(n-1, h, f, t)
    elif n==0 :
        pass
    else :
        print('The number of disks must be 0 or more.')
        sys.exit(0)

if __name__ == '__main__' :
    parser = argparse.ArgumentParser(description = 'Towers of Hanoi in recursive Python')
    parser.add_argument('-n', '--number', type = int, default = 3,
            help = 'enter the number of discs to move')
    parser.add_argument('-f', '--from', type = str, default = 'a',
            help = 'enter the name of the From source tower')
    parser.add_argument('-v', '--via', type = str, default = 'b',
            help = 'enter the name of the Via tower')
    parser.add_argument('-t', '--to', type = str, default = 'c',
            help = 'enter the name to the To target tower')

    args = parser.parse_args()
    # print(f'The arguments received are: {vars(args)}.')

    # Note the use of vars because from is a keyword.
    hanoi(args.number, vars(args)['from'], args.via, args.to)
    print(f'The number of moves is {moveCount} for {args.number} disks.')
