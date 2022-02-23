import numpy as np


#
# Methods for Bit Vector Creation
#

def zeros(dim: int):
    return np.zeros(dim, dtype=np.float64)


def ones(dim: int):
    return np.ones(dim, dtype=np.float64)


def from_int(n: int, dim: int=None):
    fmt = f'0{dim}b' if dim else '0b'
    return np.fromiter(format(n, fmt)[::-1], dtype=np.float64)


def unit(k: int, dim: int=None):
    return from_int(1 << k, dim=dim)


def from_string(string: str):
    return np.fromiter(string, dtype=np.float64)


#
# Methods for Bit Vector Destruction
#

def norm(bitvec):
    return bitvec.sum()


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
