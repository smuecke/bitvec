import numpy as np


def _is_iterable(o):
    try:
        iter(o)
        return True
    except TypeError:
        return False

#
# Methods for Bit Vector Creation
#

def zeros(dim: int):
    return np.zeros(dim, dtype=np.float64)


def ones(dim: int):
    return np.ones(dim, dtype=np.float64)


def from_int(n, dim: int=None):
    fmt = f'0{dim}b' if dim else '0b'
    if _is_iterable(n):
        return np.vstack([np.fromiter(format(n_, fmt)[::-1], dtype=np.float64) for n_ in n])
    return np.fromiter(format(n, fmt)[::-1], dtype=np.float64)


def unit(k, dim: int=None):
    return from_int(1 << k, dim=dim)


def from_string(string):
    if isinstance(string, list):
        return np.vstack([np.fromiter(s, dtype=float64) for s in string])
    return np.fromiter(string, dtype=np.float64)


#
# Methods for Bit Vector Destruction
#

def norm(bitvec):
    return bitvec.sum(-1)


def to_int(bitvec):
    return int((bitvec * 2**np.arange(bitvec.size)).sum())


def to_string(bitvec):
    return ''.join(str(int(x)) for x in bitvec)


#
# Methods for Bit Vector Transformation
#

def inv(bitvec):
    return 1-bitvec


def reverse(bitvec):
    return bitvec[::-1]


#
# Pairwise Bit Vector Methods
#

def hamming_dist(u, v, normalize=False):
    assert u.size == v.size, 'Bit vectors must have equal length'
    if normalize:
        return (u != v).sum() / u.size
    else:
        return (u != v).sum()


def cat(*args):
    return np.hstack(args)
