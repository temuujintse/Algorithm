class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        def majority_element_rec(lo: int, hi: int) -> int:
            
            if lo == hi:
                return nums[lo]

            mid = (lo + hi) // 2
            left_majority = majority_element_rec(lo, mid)
            right_majority = majority_element_rec(mid + 1, hi)

            if left_majority == right_majority:
                return left_majority

            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left_majority)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right_majority)

            return left_majority if left_count > right_count else right_majority

        return majority_element_rec(0, len(nums) - 1)