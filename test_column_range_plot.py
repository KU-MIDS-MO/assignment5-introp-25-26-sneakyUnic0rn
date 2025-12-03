import os
import numpy as np
from column_range_plot import column_range_plot

def test_column_range():
    A = np.array([[1., 4., 9.],
                  [3., 1., 5.],
                  [7., 2., 8.]])

    f = "test_column_ranges.pdf"
    if os.path.exists(f):
        os.remove(f)

    ranges = column_range_plot(A, filename=f)

    # col 0: max=7, min=1 -> 6
    # col 1: max=4, min=1 -> 3
    # col 2: max=9, min=5 -> 4
    expected = np.array([6., 3., 4.])
    np.testing.assert_allclose(ranges, expected)
    assert os.path.exists(f)

