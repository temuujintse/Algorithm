class Solution {
    public int majorityElement(int[] nums) {
        return majorityElementRec(nums, 0, nums.length - 1);
    }

    private int majorityElementRec(int[] nums, int lo, int hi) {
        if (lo == hi) {
            return nums[lo];
        }
        int mid = (lo + hi) / 2;

        int leftMajority = majorityElementRec(nums, lo, mid);
        int rightMajority = majorityElementRec(nums, mid + 1, hi);

        if (leftMajority == rightMajority) {
            return leftMajority;
        }

        int leftCount = 0, rightCount = 0;
        for (int i = lo; i <= hi; i++) {
            if (nums[i] == leftMajority) {
                leftCount++;
            } else if (nums[i] == rightMajority) {
                rightCount++;
            }
        }

        return leftCount > rightCount ? leftMajority : rightMajority;
    }
}
