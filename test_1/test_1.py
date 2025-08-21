def is_even(number: int) -> bool:
    """
    Returns True if the input number is even, False otherwise.
    """
    return number % 2 == 0

# open Week 6 folder
# pytest "test_1\test_1.py"

# Test cases for is_even function
# Positive even numbers

def test_1():
    assert is_even(2) == True

def test_2():
    assert is_even(10) == True

# Positive odd numbers
def test_3():
    assert is_even(3) == False

def test_4():
    assert is_even(17) == False

# Zero (special case - even number)
def test_5():
    assert is_even(0) == True

# Negative numbers
def test_6():
    assert is_even(-2) == True

def test_7():
    assert is_even(-7) == False

print(" All test cases passed!")