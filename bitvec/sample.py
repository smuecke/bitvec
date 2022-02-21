import itertools

import numpy as np

from .misc import _get_random_state, _format_shape, binom


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


#
# Bit Vector Generators
#


class BitvecGenerator:
    def __iter__(self):
        return self


class all(BitvecGenerator):
    def __init__(self, dim: int, read_only=True):
        self.__dim = dim
        self.__read_only = read_only
        self.__vec = np.zeros(self.__dim, dtype=np.float64)

    def __iter__(self):
        self.__vec = np.zeros(self.__dim, dtype=np.float64)
        while True:
            yield self.__vec if self.__read_only else self.__vec.copy()
            pointer = 0
            while self.__vec[pointer] == 1.0:
                self.__vec[pointer] = 0.0
                pointer += 1
                if pointer >= self.__dim:
                    return
            self.__vec[pointer] = 1.0


class all_with_norm(BitvecGenerator):
    def __init__(self, dim: int, norm):
        self.__dim = dim
        try:
            self.__norms = list(sorted({ k for k in norm if 0 <= k <= dim }))
        except TypeError:
            self.__norms = [ norm ]

    def __iter__(self):
        x = np.empty(self.__dim, dtype=np.float64)
        for k in self.__norms:
            for ixs in itertools.combinations(np.arange(self.__dim), r=k):
                x[:] = 0.0
                x[(ixs,)] = 1.0
                yield x.copy()


#
# Bit Vector Samplers
#


class BitvecSampler(BitvecGenerator):
    def sample(self, n: int=1):
        raise NotImplementedError()

    def __call__(self, n: int=1):
        return self.sample(n)

    def __next__(self):
        return self.sample()


class uniform(BitvecSampler):
    def __init__(self, dim: int, p: float=0.5, random_state=None):
        self.__dim   = dim
        self.__p     = p
        self.__state = _get_random_state(random_state)

    def sample(self, n: int=1):
        s = _format_shape(n, self.__dim)
        return self.__state.binomial(1, self.__p, size=s).astype(np.float64)
    

class with_norm(BitvecSampler):
    def __init__(self, dim: int, norm, equiprobable_norms=False, random_state=None):
        self.__dim = dim
        try:
            self.__norms = list({k for k in norm if 0<=k<=dim})
        except TypeError:
            self.__norms = [norm]

        if equiprobable_norms:
            # all norms appear equally likely
            self.__probs = [1/len(self.__norms)]*len(self.__norms)
        else:
            # all norms appear proportionally to the total number
            # of bit vectors with that norm
            num_vecs = [ binom(dim, k) for k in self.__norms ]
            total = sum(num_vecs)
            self.__probs = [ n/total for n in num_vecs ]
        self.__state = _get_random_state(random_state)

    def sample(self, n: int=1):
        norms = self.__state.choice(self.__norms, p=self.__probs, size=(n,))
        arr = np.resize(np.arange(self.__dim), (n, self.__dim))
        arr = np.apply_along_axis(self.__state.permutation, axis=1, arr=arr)
        arr = (arr < norms[:, np.newaxis]).astype(np.float64)
        return arr if n > 1 else arr[0]


class ising(BitvecSampler):
    def __init__(self, gen: BitvecSampler):
        self.__gen = gen

    def sample(self, n: int=1):
        return 2*self.__gen.sample(n)-1

    def __next__(self):
        return 2*next(self.__gen)-1
