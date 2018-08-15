#!/usr/bin/env python
from enum import Enum

import numpy as np
from random import randint

class Naipe(Enum):
    COPAS = 1
    OUROS = 2
    ESPADAS = 3
    PAUS = 4


def main():
    """Exemplo da biblioteca numpy"""

    # Array em numpy
    v1 = np.array([1, 4, 6, 7, 9, 0])
    v2 = np.array([1.0, 4.3, 6.9, 7.3, 9.9, 0])
    v3 = np.zeros(10)
    v4 = np.ones(10)
    v5 = np.empty((2, 2))

    print(v1)
    print(v3)
    print(v4)
    print(v5)

    print(v1.dtype)
    print(v2.dtype)

    m1 = np.array([
        [randint(0, 10) for x in range(1, 5)],
        [randint(0, 10) for x in range(1, 5)],
        [randint(0, 10) for x in range(1, 5)],
    ])

    print(m1)

    a = np.array([randint(0, 9) for x in range(5)])
    b = np.array([randint(0, 9) for x in range(5)])

    print(a)
    print(b)
    print(a+b)
    print(a**2)
    print(a < 5)
    print(a.sum())
    print(a.mean())
    print(a.max())
    print(a.min())




if __name__ == '__main__':
    main()