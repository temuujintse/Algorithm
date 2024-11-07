class Solution:
    def numTrees(self,n: int) -> int:
       
        numTree = [0] * (n + 1)
    
        numTree[0] = numTree[1] = 1
        
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                numTree[i] += numTree[j - 1] * numTree[i - j]
        
        return numTree[n]
