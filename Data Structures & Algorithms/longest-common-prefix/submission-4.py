class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        prefix = strs[0]

        for i in range(1, len(strs)):
            if strs[i] == "":
                return ""
            count = 0
            for j in range(min(len(strs[i]), len(prefix))):
                
                if strs[i][j] != prefix[j]:
                    break
                count+=1
            prefix = prefix[0:count]
        return prefix



            