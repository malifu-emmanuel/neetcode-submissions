class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        

        temp = []
        temp.append(nums[0])

        for i in range(1, len(nums)):
            if temp[-1]!= nums[i]:
                temp.append(nums[i])
        
        for i in range(len(temp)):
            nums[i]=temp[i]
        return len(temp)
        

