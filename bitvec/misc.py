from hashlib import md5

import numpy as np


def _format_shape(n, dim: int):
    if (n is None) or (n == 1):
        return (dim,)
    try:
        return (*n, dim)
    except TypeError:
        return (n, dim)


def _format_seed(seed):
    try:
        seed_ = int(seed)
    except ValueError:
        bseed = str(seed).encode('utf-8')
        seed_ = int(md5(bseed).digest().hex(), 16) % (2**32)
    return seed_


def _get_random_state(obj):
    if obj is None:
        # return unseeded random state
        return np.random.RandomState()
    if isinstance(obj, np.random.mtrand.RandomState):
        return obj
    else:
        # interpret as seed
        seed = _format_seed(obj)
        return np.random.RandomState(seed)


def binom(n, k):
    return np.math.factorial(n) // (np.math.factorial(k)*np.math.factorial(n-k))
