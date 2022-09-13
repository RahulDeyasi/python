class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo={}
        def dp(n):
            if n==0:
                return 0
            if n==1:
                return nums[0]
            if n in memo:
                return memo[n]
            else:
                memo[n]=max(dp(n-1),dp(n-2)+nums[n-1])
            return memo[n]
        return dp(len(nums))
