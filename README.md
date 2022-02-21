# `bitvec`

A Python toolbox for binary vectors.

## Installation

Install this package by running `pip install git+https://github.com/smuecke/bitvec.git` in your console.


## Examples

This is code for iterating over all binary vectors of length `10`:
```
>> from bitvec import all
>> for x in all(10):
    do_stuff(x)
```

By default, all bit vectors are numpy arrays of type `numpy.float64` containing only `0.0` and `1.0`.
Most methods are shallow wrappers around numpy functions, so this package is more of a toolbox.

Here are some ways to sample bit vectors:
```
>> from bitvec import uniform, with_norm
>> # sample 100 bit vectors of size 20 uniformly
>> sampler = uniform(20)
>> sampler(100)
array([[1., 1., 1., ..., 1., 0., 0.],
       [0., 1., 1., ..., 1., 1., 0.],
       [1., 0., 0., ..., 1., 0., 1.],
       ...,
       [0., 1., 0., ..., 1., 0., 0.],
       [1., 1., 1., ..., 1., 1., 0.],
       [0., 0., 0., ..., 0., 0., 1.]])
>>
>> # sample 5 vectors of size 30 with 15 or 16 one-bits in them
>> sampler = with_norm(10, [5, 6])
>> sampler(5)
array([[0., 1., 0., 1., 1., 0., 1., 0., 1., 0.],
       [1., 0., 0., 1., 0., 1., 0., 1., 1., 0.],
       [0., 1., 1., 1., 0., 1., 0., 0., 0., 1.],
       [0., 1., 1., 0., 1., 1., 0., 1., 0., 0.],
       [0., 1., 1., 1., 1., 0., 1., 0., 1., 0.]])
```

You can also easily create, modify and analyse bit vectors, e.g.
```
>> from bitvec import from_int, hamming_dist, to_int, reverse
>> u, v = from_int(238, 10), from_int(239, 10)
>> u
array([0., 1., 1., 1., 0., 1., 1., 1., 0., 0.])
>> v
array([1., 1., 1., 1., 0., 1., 1., 1., 0., 0.])
>> hamming_dist(u, v)
1
>> to_int(reverse(v))
988
```

Documentation coming soon!
