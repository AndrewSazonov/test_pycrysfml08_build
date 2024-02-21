import os
import sys
from numpy.testing import assert_almost_equal

sys.path.append(os.path.join('PyCrysFML08_install','pycrysfml08'))
from pycrysfml08 import py_cfml_profiles

# Tests

def test_exponential():
    alfa = 1.0
    x = 1.5
    desired = alfa * math.exp(-alfa * x)
    actual = py_cfml_profiles.exponential(x, alfa)[2]
    assert_almost_equal(desired, actual, decimal=3, verbose=True)
