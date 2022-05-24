#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    number = int(input("Введите номер месяца: "))
    if number < 1 or number > 12:
        print("Ошибка!", file=sys.stderr)
        exit(1)
    else:
        if number == 2:
            print("28 дней")
        elif number % 2 == 1:
            print("31 день")
        else:
            print("30 дней")
