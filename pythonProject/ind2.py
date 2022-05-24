#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    x, y = int(input("Enter the x: ")), int(input("Enter the y: "))
    if pow(x, 2) * y > x * pow(y, 2):
        Max = pow(x, 2) * y
    else:
        Max = x * pow(y, 2)
    if x - y < x + 2 * y:
        Min = x - y
    else:
        Min = x + 2 * y
    print(f"U = {pow(Max, 2) + pow(Min, 2)}")
