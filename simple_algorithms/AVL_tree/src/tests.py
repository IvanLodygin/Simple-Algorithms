from main import insert_value, is_balanced, delete_value, print_tree
from random import randint
import time

test_data_10 = [randint(0, 100) for _ in range(10)]
test_data_1000 = [randint(0, 100) for _ in range(1000)]
test_data_100000 = [randint(0, 100) for _ in range(100000)]

def measure_insert_time(data):
    tree = None
    start_time = time.time()
    for value in data:
        tree = insert_value(value, tree)
    elapsed_time = time.time() - start_time
    assert is_balanced(tree), "Tree is not balanced after insertion"
    return elapsed_time

def measure_delete_time(data):
    tree = None
    for value in data:
        tree = insert_value(value, tree)

    start_time = time.time()
    for value in data:
        tree = delete_value(value, tree)
    elapsed_time = time.time() - start_time
    assert is_balanced(tree), "Tree is not balanced after deletion"
    return elapsed_time

print(f"Insertion time for 10 elements: {measure_insert_time(test_data_10):.6f} seconds")
print(f"Insertion time for 1000 elements: {measure_insert_time(test_data_1000):.6f} seconds")
print(f"Insertion time for 100000 elements: {measure_insert_time(test_data_100000):.6f} seconds")

print(f"Deletion time for 10 elements: {measure_delete_time(test_data_10):.6f} seconds")
print(f"Deletion time for 1000 elements: {measure_delete_time(test_data_1000):.6f} seconds")
print(f"Deletion time for 100000 elements: {measure_delete_time(test_data_100000):.6f} seconds")
