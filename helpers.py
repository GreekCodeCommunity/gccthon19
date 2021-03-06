import numpy as np

from functools import reduce, partial

def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

array = compose(np.array, tuple)

def arr(m):
    return array(m)

def mapt(f, l):
    return compose(array, partial(map, f))(l)

def countif(f, l):
    return compose(len, array, partial(filter, f))(l)

def append(acc, l):
    return np.append(acc, l, axis=0)

def add(x, y):
    return x+y

def identity(x):
	return x

def flatten(x):
    return reduce(append, x)
