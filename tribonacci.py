class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo={}
        def fibmemo(n):
            if n in memo:
                return memo[n]
            if(n==0):
                memo[n]=0
            elif(n==1 or n==2):
                memo[n]=1
            elif(n!=0):
                memo[n]=fibmemo(n-3)+fibmemo(n-3+1)+fibmemo(n-3+2)
            return memo[n]
        return fibmemo(n)
a=Solution()
n=int(input())
print(a.tribonacci(n))
