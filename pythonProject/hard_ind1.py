#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# Постоянная Эйлера.
EULER = 0.5772156649015328606
# Точность вычислений.
EPS = 1e-10

if __name__ == '__main__':
    x = int(input("Enter thr x: "))
    a = -(pow(x, 2)) / 4
    n = 1
    s = a
    while abs(a) > EPS:
        a *= -(n * pow(x, 2)) / (4 * pow(n, 3) + 10 * pow(n, 2) + 8 * n + 2)
        s += a
        n += 1
    print(f"Ci({x}) = {EULER + math.log(x) + s}")
