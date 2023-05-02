#!/usr/bin/env python

import numpy as np
import numpy.linalg as la

A = np.array(object=[[3, 2, 2], [2, 3, -2]], dtype=np.float64)


def choose_B(A: np.array):
    m, n = A.shape
    print(f"Si A tiene {m} filas y {n} columnas,")

    if (A.T @ A).shape < (A @ A.T).shape:
        B = A.T @ A
        print(f"entonces, escogemos A^T * A de orden {B.shape[0]} x {B.shape[1]}.")
        return B
    else:
        B = A @ A.T
        print(f"entonces, escogemos A * A^T de orden {B.shape[0]} x {B.shape[1]}.")
        return B


B = choose_B(A)

# Prueba si la matriz es cuadrada
assert B.shape[0] == B.shape[1] > 0
# Prueba si la matriz es simetrica
assert abs((B - B.T).max()) < 1e-14


if __name__ == "__main__":
    print()
