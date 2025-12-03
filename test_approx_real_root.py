import numpy as np
from approx_real_root import *

def test_approx_real_root():
    # Polynomial: q(x) = 1 - 4x + x^3
    coeffs = [1, -4, 0, 1]
    interval = (0.0, 1.0)

    root = approx_real_root(coeffs, interval)

    expected = 0.254101688365052
    assert np.isclose(root, expected, atol=1e-9), \
        f"Expected approximately {expected}, got {root}"

