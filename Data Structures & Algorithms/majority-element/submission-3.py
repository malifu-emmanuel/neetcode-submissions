class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if len(nums) <=2:
            return nums[0]
        ans = {}

        for i in range(len(nums)):
            if nums[i] in ans:
                ans[nums[i]] += 1
                if ans[nums[i]] >= len(nums)//2 + 1:
                    return nums[i]
            else:
                ans[nums[i]] = 1
            
        return 0

        
        