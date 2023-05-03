#!/usr/bin/env python

import numpy as np
import numpy.linalg as la

B = np.array(object=[[4, 2, 6], [2, 2, 5], [6, 5, 29]], dtype=np.float64)


def corner_matrices(A: np.array):
    # Prueba si la matriz es cuadrada
    assert A.shape[0] == A.shape[1] > 0
    # Prueba si la matriz es simetrica
    assert abs((A - A.T).max()) < 1e-14

    for k in range(B.shape[0]):
        print(f"|A_{k+1}|={la.det(B[: k + 1, : k + 1])}")


if __name__ == "__main__":
    corner_matrices(B)
