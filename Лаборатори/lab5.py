import unittest

def fibonacci_memoization(n, memo={}):

    if n in memo:
        return memo[n] 

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci_memoization(0), 0)
        self.assertEqual(fibonacci_memoization(1), 1)
        self.assertEqual(fibonacci_memoization(10), 55)
        self.assertEqual(fibonacci_memoization(16), 987)

if __name__ == '__main__':
    unittest.main()