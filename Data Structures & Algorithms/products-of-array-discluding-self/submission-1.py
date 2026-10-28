class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def prod_find(nums):
            prod = 1
            for i in range(len(nums)):
                prod*=nums[i]
            return prod

        output = []
        
        prod= prod_find(nums)
        zindex = -1
        for i in range(len(nums)):
            
            if nums[i]==0:
                temp = [0]*len(nums)
                temp[i] = prod_find(nums[0:i])*prod_find(nums[i+1:])
                return temp
            output.append(int(prod/nums[i]))
        
        return output