class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count+=1

        for i in range(len(nums)-count):
  
                for j in range(len(nums)-1,0,-1):
                    if nums[j]!=val:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        break
        return len(nums)-count
