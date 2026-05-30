class Solution:
    def isPalindrome(self, s: str) -> bool:
        
     punctuation = "!@#$%^&*()?.,<>/';:=+--}{[]~`}"
     s = (''.join(ch for ch in s if not ch in punctuation)).lower().replace(" ", "")

     print(s)

     i=0
     j=len(s)-1 

     while i <=j:
        print(i,j)
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
       
    
     return True
        
