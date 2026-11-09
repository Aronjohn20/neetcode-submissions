class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        j=0
        while j < len(nums):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i=i+1
                j=j+1
            elif nums[j]==0:
                j=j+1

        return nums

        