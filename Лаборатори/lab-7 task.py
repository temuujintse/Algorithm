import unittest
from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskC = Counter(tasks)
        maxC = max(taskC.values())
        maxTask = list(taskC.values()).count(maxC)
        
        return max(len(tasks), (maxC - 1) * (n + 1) + maxTask)

class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()
    
    def test_case_1(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        self.assertEqual(self.sol.leastInterval(tasks, n), 8)

    def test_case_2(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 0
        self.assertEqual(self.sol.leastInterval(tasks, n), 6)
    
    def test_case_3(self):
        tasks = ["A", "A", "A", "A", "B", "B", "C", "C", "D", "D"]
        n = 2
        self.assertEqual(self.sol.leastInterval(tasks, n), 10)

    def test_case_4(self):
        tasks = ["A", "B", "C", "D", "E", "F", "G"]
        n = 3
        self.assertEqual(self.sol.leastInterval(tasks, n), 7)

if __name__ == '__main__':
    unittest.main()
