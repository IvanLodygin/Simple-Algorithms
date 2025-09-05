import random
from main import timsort

def check_timsort():
    data = [random.randint(0, 100) for _ in range(100)]
    expected_result = sorted(data, reverse=True)
    result_from_custom = timsort(data)
    assert result_from_custom == expected_result, "Sorting failed!"

check_timsort()