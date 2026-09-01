class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hmap = {}

        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]]+=1
            else:
                hmap[nums[i]]=1
        ans = []
        for i in range(len(hmap)):
            if len(ans) == k:
                break
            max_val = -1001
            max_key = 0
            for key,val in hmap.items():
                if val>max_val:
                    max_val = val
                    max_key = key
          
            ans.append(max_key)
            hmap.pop(max_key)

        return ans




        