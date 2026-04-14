import os

def generate_test():
    # Simulated LLM output (for POC)
    test_code = """
import time
from src.sample import slow_function

def measure(func, data):
    start = time.time()
    func(data)
    return time.time() - start

def test_auto_generated():
    small = list(range(1000))
    large = list(range(5000))

    t1 = measure(slow_function, small)
    t2 = measure(slow_function, large)

    assert t2 < t1 * 20
"""

    os.makedirs("tests/performance", exist_ok=True)

    with open("tests/performance/test_auto_generated.py", "w") as f:
        f.write(test_code)

    print("✅ Auto-generated performance test")

if __name__ == "__main__":
    generate_test()
