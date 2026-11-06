class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            result[nums[i]] = i
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i!=j:
                    return [result[nums[i]],j]
                    
        