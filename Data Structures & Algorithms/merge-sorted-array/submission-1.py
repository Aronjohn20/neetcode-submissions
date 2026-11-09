class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        t = m+n
        i=0
        j=0
        while(i<t and j<n):
            if nums1[i]!=0:
                i=i+1
            elif nums1[i]==0:
                nums1[i],nums2[j]=nums2[j],nums1[i]
                i=i+1
                j=j+1

        nums1.sort()
        return nums1 
       