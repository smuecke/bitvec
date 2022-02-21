import numpy as np


#
# Methods for Bit Vector Destruction
#

def norm(bitvec):
    return bitvec.sum()


def to_int(bitvec):
    return int((bitvec * 2**np.arange(bitvec.size)).sum())


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
