"""Tests for utility methods in subset module
"""
from nose.tools import istest, raises

from jasmin_cis.subsetting.subset import Subset

# Tests for _fix_longitude_limits
@istest
def test01_for_0_to_360():
    result = Subset._fix_longitude_limits(0, 90, 0, 360)
    assert (result == (0, 90))


@istest
def test02_for_0_to_360():
    result = Subset._fix_longitude_limits(10, 350, 0, 360)
    assert (result == (10, 350))


@istest
def test03_for_0_to_360():
    result = Subset._fix_longitude_limits(0, 359.9, 0, 360)
    assert (result == (0, 359.9))


@istest
def test04_for_0_to_360():
    result = Subset._fix_longitude_limits(180, 359.9, 0, 360)
    assert (result == (180, 359.9))


@istest
def test05_for_0_to_360():
    result = Subset._fix_longitude_limits(0, 360, 0, 360)
    assert (result == (0, 360))


@istest
def test06_for_0_to_360():
    result = Subset._fix_longitude_limits(0, 0, 0, 360)
    assert (result == (0, 0))


@istest
def test07_for_0_to_360():
    result = Subset._fix_longitude_limits(360, 360, 0, 360)
    assert (result == (360, 360))


@istest
def test08_for_0_to_360():
    result = Subset._fix_longitude_limits(0.1, -0.1, 0, 360)
    assert (result == (0.1, 359.9))


@istest
def test09_for_0_to_360():
    result = Subset._fix_longitude_limits(-1, 359, 0, 360)
    assert (result == (359, 359))


@istest
def test10_for_0_to_360():
    result = Subset._fix_longitude_limits(-1, 359, 0, 360)
    assert (result == (359, 359))


@istest
def test01_for_minus180_to_180():
    result = Subset._fix_longitude_limits(0, 0, -180, 180)
    assert (result == (0, 0))


@istest
def test02_for_minus180_to_180():
    result = Subset._fix_longitude_limits(-180, -180, -180, 180)
    assert (result == (-180, -180))


@istest
def test03_for_minus180_to_180():
    result = Subset._fix_longitude_limits(180, 180, -180, 180)
    assert (result == (180, 180))


@istest
def test04_for_minus180_to_180():
    result = Subset._fix_longitude_limits(-180, 180, -180, 180)
    assert (result == (-180, 180))


@istest
def test05_for_minus180_to_180():
    result = Subset._fix_longitude_limits(1, -180.1, -180, 180)
    assert (result == (1, 179.9))


@istest
def test06_for_minus180_to_180():
    result = Subset._fix_longitude_limits(181, 179, -180, 180)
    assert (result == (-179, 179))


# Ambiguous as to whether 0,360 or -180,180
@istest
def test01_for_0_to_180():
    result = Subset._fix_longitude_limits(0, 180, 0, 180)
    assert (result == (0, 180))


@istest
def test02_for_0_to_180():
    result = Subset._fix_longitude_limits(0, 360, 0, 180)
    assert (result == (0, 0))


@istest
def test01_for_minus1_to_180():
    result = Subset._fix_longitude_limits(181, 179, -1, 180)
    assert (result == (-179, 179))


if __name__ == '__main__':
    import nose
    nose.runmodule()