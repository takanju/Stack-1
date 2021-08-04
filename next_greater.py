"""
        TC:O(4n)
        SC:O(n)
        """
        n=len(nums)
        res=[-1]*n
        s=[0]
        for i in range(1, 2*n):
            while s and nums[i%n] > nums[s[-1]]:
                idx=s.pop()
                res[idx]=nums[i%n]
            if i<n:
                s.append(i)
        return res