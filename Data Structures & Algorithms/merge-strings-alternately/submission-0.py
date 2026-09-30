class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        

        bigword = ""
        min_len = min(len(word1),len(word2))
        for i in range(min_len):

            bigword += word1[i]+word2[i]
        
        return bigword+ word1[min_len:] if len(word1)>len(word2) else bigword+word2[min_len:]