class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t = set()
        num = 0
        left = 0
        right = 0
        n = len(s)
        for right in range(n):
            while s[right] in t:
                t.remove(s[left])
                left+=1

            t.add(s[right])
            # right+=1
            num = max(num,right-left+1)

        return num
            
            
        