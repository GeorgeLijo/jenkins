def add_numbers(a, b):
    """
    Function to add two numbers.
    Intentionally returns an incorrect result for testing failure.
    """
    return a + b + 1  # Incorrect logic: adds an extra 1

# Test case
def test_add_numbers():
    assert add_numbers(2, 3) == 5, "Test failed: 2 + 3 should be 5"
    assert add_numbers(-1, 1) == 0, "Test failed: -1 + 1 should be 0"
    assert add_numbers(0, 0) == 0, "Test failed: 0 + 0 should be 0"

# Run test
if __name__ == "__main__":
    test_add_numbers()
