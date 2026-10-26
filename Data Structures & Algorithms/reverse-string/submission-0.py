class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_len = len(s)
        end = s_len
        for i in range(s_len//2):
            end-=1
            temp = s[i]
            s[i] =s[end]
            s[end]= temp
        
                
        


            

