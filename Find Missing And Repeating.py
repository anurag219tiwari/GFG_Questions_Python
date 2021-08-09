"""
My approach: 
1. Maintain a dictionary (nums) to keep a count of total occurences of each element
2. Initialize the key values in dictionary from 1 to n and their corresponding values to 0
3. Traverse the array and increment the key value in nums, for the corresponding array's element's value
4. Traverse the dictionary again to check the keys for which the values are 0 (missing) and 2 (repeating)
5. Return these key values

"""
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
