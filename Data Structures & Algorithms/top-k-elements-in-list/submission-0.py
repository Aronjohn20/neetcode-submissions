class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        m = []
        for n in nums:
            s[n] = s.get(n,0) + 1
        
        for g,c in s.items():
            m.append([c,g])

        m.sort()

        res=[]
        while len(res) < k:
            res.append(m.pop()[1])

        return res

            


        

        

        
        
        