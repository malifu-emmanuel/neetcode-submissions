class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        temp = []

        for num in nums:
            
            if num != val:
                temp.append(num)

        for i in range(len(nums)):
            if i< len(temp):
                nums[i] = temp[i]
            else:
                nums[i] = 0
        return len(temp)