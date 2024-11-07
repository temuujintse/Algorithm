class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        if len(s) < 2:
            return ""
        
        for i, char in enumerate(s):
            if char.swapcase() not in s:
                
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                
                return left if len(left) >= len(right) else right
        return s