class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        TC:O(n)
        SC:O(n)
        """
        t=temperatures
    
        s=[0]
        res=[0]*len(t)
        for i in range(1, len(t)):
            while s and t[i]>t[s[-1]]:
                idx=s.pop()
                res[idx]=i-idx
            s.append(i)
        return res