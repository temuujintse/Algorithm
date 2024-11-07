class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] newCost = new int[cost.length + 1];
        System.arraycopy(cost, 0, newCost, 0, cost.length);
        newCost[cost.length] = 0; 

        for (int i = newCost.length - 3; i >= 0; i--) {
            newCost[i] += Math.min(newCost[i + 1], newCost[i + 2]);
        }

        return Math.min(newCost[0], newCost[1]);
    }
}