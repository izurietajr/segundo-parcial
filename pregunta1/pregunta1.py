#!/usr/bin/env python3

import sys
import random
import math
import numpy as np


inp = np.array([1, 2, 3, 4, 5])

# funciones de activación
sigmoid = lambda x: 1/(1+np.exp(-x))
relu = lambda x: max(0, x)


def gen_random_array(w: int):
    return np.array([random.random() for _ in range(w)])

def gen_random_matrix(w: int, h: int):
    weights = np.matrix(
        [
            gen_random_array(w)
            for _ in range(h)
        ]
    )
    return weights


biases = np.array([random.random() for _ in range(5)])


def main(args=None):
    pass


if __name__ == '__main__':
    main(sys.argv)
