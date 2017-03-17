import numpy as np

def kmax2d(arr, k):
    """Return the (row, col) indices of the n largest arguments in the 2d array.

    Parameters
    ----------
    arr : array
        2d numpy array
    k : int
        number of arguments to select.

    Returns
    -------
    row : array
        indices
    col : array
    """
    n, m = arr.shape
    vec = arr.flatten()
    vec_ = vec.argsort()[::-1]
    top_vec = vec_[:k]
    row = top_vec // n
    col = top_vec % n
    return row, col
