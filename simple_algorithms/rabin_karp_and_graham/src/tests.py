from modules.rabin_karp import search_patterns
from modules.graham import graham, area

def test_rabin_karp():
    pattern = "lar"
    text = "lar fff lar lar"
    assert search_patterns(pattern, text) == [0, 8, 12], "Test failed for Rabin-Karp"

def test_graham():
    dots = [[1, 1], [3, 4], [5, 2], [2, 2], [4, 4], [0, 0]]
    expected_hull = [[0, 0], [5, 2], [4, 4], [3, 4]] 
    expected_area = 8.0

    hull, hull_area = graham(dots), area(expected_hull)
    
    assert hull == expected_hull, f"Expected {expected_hull}, got {hull}"
    
    assert abs(hull_area - expected_area) < 1e-6, f"Expected area {expected_area}, got {hull_area}"

test_rabin_karp()
print("Rabin-Karp test passed")

test_graham()
print("Graham-Scan test passed")