"""
Tests for test_project.
"""

import os
from pathlib import Path
from typing import Optional

import pytest
import numpy as np
from numpy.testing import assert_array_equal

from test_project.demo import main


THIS_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
EXPECTED_OUTPUTS_DIR = THIS_DIR / "expected_outputs"


def _save_test_regression():
    """
    Save demo results for regression test.
    """
    out1, out2, out3 = main(show=False)
    np.save(EXPECTED_OUTPUTS_DIR / "out1.npy", out1)
    np.save(EXPECTED_OUTPUTS_DIR / "out2.npy", out2)
    np.save(EXPECTED_OUTPUTS_DIR / "out3.npy", out3)


def test_regression():
    """
    Compare current output with expected.
    """
    out1, out2, out3 = main(show=False)

    expected_out1 = np.load(EXPECTED_OUTPUTS_DIR / "out1.npy")
    expected_out2 = np.load(EXPECTED_OUTPUTS_DIR / "out2.npy")
    expected_out3 = np.load(EXPECTED_OUTPUTS_DIR / "out3.npy")

    assert_array_equal(out1, expected_out1)
    assert_array_equal(out2, expected_out2)
    assert_array_equal(out3, expected_out3)


@pytest.mark.parametrize("img_size", [None, (64, 64), (256, 256)])
def test_no_error(img_size: Optional[tuple[int, int]]):
    """
    Test demo on different image sizes.
    """
    print(main.__code__.co_argcount)
    main(img_size=img_size, show=False)
