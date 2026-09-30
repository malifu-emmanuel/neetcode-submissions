class Solution:
    


    def validPalindrome(self, s: str) -> bool:
        
        def validP(s:str) -> bool:

            for i in range(len(s)//2):
                if s[i]!= s[len(s)-1-i]:
                    return False
            return True
        
        for i in range(len(s)):
            word = ''
            for j in range(len(s)):
                if j != i:
                    word +=s[j]

            if validP(word):
                
                return True
        

        return False

        