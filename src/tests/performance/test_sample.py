import time
from src.sample import slow_function

def measure(func, data):
    start = time.time()
    func(data)
    return time.time() - start

def test_performance():
    small = list(range(1000))
    large = list(range(5000))

    t1 = measure(slow_function, small)
    t2 = measure(slow_function, large)

    assert t2 < t1 * 20
