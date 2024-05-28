import pytest
import time

def test_1_part1():
    time.sleep(5)

def test_2_part1():
    time.sleep(5)
    pytest.xfail()

def test_3_part1():
    time.sleep(5)
    pytest.skip()
