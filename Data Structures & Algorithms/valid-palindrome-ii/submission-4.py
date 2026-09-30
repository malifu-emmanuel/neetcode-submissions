class Solution:
    


    def validPalindrome(self, s: str) -> bool:
        
        def validP(s:str) -> bool:

            for i in range(len(s)//2):
                if s[i]!= s[len(s)-1-i]:
                    return False
            return True
        if validP(s):
            return True

        for i in range(len(s)//2):

            if s[i]!= s[len(s)-1-i]:
                word1 = s[:i]+s[i+1:]
                word2 = s[:len(s)-1-i]+ s[len(s)-1-i+1:]
                return validP(word1) or validP(word2)

        return False

        