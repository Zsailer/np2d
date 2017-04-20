# Np2d: 2-D NumPy operations

I find that 2-D arrays are pretty common in scientific computing, and there are a few
operations I find myself repeatedly writing for 2-D array. While simple, these operations
are too specific for the general NumPy scope (and thus, do not warrant a pull request).
So, I'm collecting a set of fast, 2-D NumPy operations here. Maybe you'll find them
useful too.

## List of functions

### `np2d.random.choice()`

Choose random samples from a 2-D array. Get the samples and their indices.

```python
import numpy as np
import np2d

a = np.random.uniform(size=(4,5))
weights =
samples, indices = np2d.random.choice(a)
```

### `np2d.kmin()`

Find the `k` smallest elements in the 2-D array.

```python
import numpy as np
import np2d

a = np.random.uniform(size=(4,5))
k_smallest_elements, indices = np2d.kmin(a, 3)
```


### `np2d.kmax()`

```python
import numpy as np
import np2d

a = np.random.uniform(size=(4,5))
k_largest_elements, indices = np2d.kmax(a, 3)
```

## Installation

To install the latest release from PyPi:
```
pip install np2d
```

To install a development version, clone this repo and install from the command line:
```
pip install -e .
```

## Suggestions

If there is a NumPy function or module you'd like extended to 2-D, or a new NumPy-like operation
you'd like me to add to this package, feel free to open an [Issue](https://github.com/Zsailer/np2d/issues/new).

## Tests

To run tests for np2d, run:

```
nosetests
```
