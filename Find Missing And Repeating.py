class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        nums = {}
        ans,ans1 = 0,0
        for i in range(1,n+1):
            nums[i] = 0
        for i in arr:
            nums[i] += 1
        for i in nums:
            if nums[i] == 0:
                ans = i
            if nums[i] == 2:
                ans1 = i
        return [ans1,ans]
