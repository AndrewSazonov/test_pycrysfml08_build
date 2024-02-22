import os
import sys
import math
import numpy as np
from numpy.testing import assert_almost_equal

sys.path.append(os.path.abspath('PyCrysFML08_install'))
from pycrysfml08 import py_cfml_metrics

# Tests

def test_get_u_from_b():
    desired = np.array([0.019, 0.0203, 0.0215, 0.0127, 0.0139, 0.0152], dtype='f')
    code, message, actual = py_cfml_metrics.get_u_from_b(np.array([1.5, 1.6, 1.7, 1.0, 1.1, 1.2], dtype='f'))
    assert code == 0
    assert message == ''
    assert_almost_equal(desired, actual, decimal=4, verbose=True)
