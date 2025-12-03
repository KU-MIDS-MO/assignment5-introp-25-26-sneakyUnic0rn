import os
import numpy as np
from detect_turning_points import detect_turning_points

def test_turning_points():
    ##example signal with multiple direction changes:
    # 1 → 4 (up), 4 → 2 (down), 2 → 5 (up), 5 → 3 (down), 3 → 6 (up)
    signal = np.array([1, 4, 2, 5, 3, 6])

    filename = "test_turning_points.pdf"
    if os.path.exists(filename):
        os.remove(filename)

    turning_indices = detect_turning_points(signal, filename=filename)

    ##directions: +, -, +, -, +
    ##sign changes at: between 0–1, 1–2, 2–3, 3–4 → indices 1,2,3,4
    expected = np.array([1, 2, 3, 4])
    np.testing.assert_array_equal(turning_indices, expected)
    assert os.path.exists(filename)
