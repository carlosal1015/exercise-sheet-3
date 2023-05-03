#!/usr/bin/env python

import numpy as np
import numpy.linalg as la

A = np.array(object=[[1, 0], [1, 1j], [0, 1j]])
rango = la.matrix_rank(A)
u, s, vh = np.linalg.svd(A, full_matrices=True)

if __name__ == "__main__":
    print(f"El rango de A es {rango}.")
    print(f"u =\n{u}")
    print(f"s =\n{s}")
    print(f"vh =\n{vh}")
