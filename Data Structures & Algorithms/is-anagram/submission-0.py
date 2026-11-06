class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        si = {}
        ti = {}
        for a in s:
            si[a] = si.get(a,0) + 1

        for j in t:
            ti[j] = ti.get(j,0) + 1

        if si==ti:
            return True
        else:
            return False     