class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = {}
        for  i in nums:
            n[i] = n.get(i,0) + 1

        for key,value in n.items():
            if n[key] > 1:
                return True

        return False
    
        