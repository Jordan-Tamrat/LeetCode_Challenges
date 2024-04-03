class Solution:
    def reverseString(self, s: List[str]) -> None:
        y=len(s)-1
        x=0
        while x < y :
            s[x],s[y]=s[y],s[x]
            x+=1
            y-=1
        return s
            
        