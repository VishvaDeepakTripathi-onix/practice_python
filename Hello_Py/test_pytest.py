import Incr_Desc    # The code to test


def test_increment():
    assert Incr_Desc.increment(3) == 4


# This test is designed to fail for demonstration purposes.
def test_decrement():
    assert Incr_Desc.decrement(3) == 4