class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        a=[x for x in range(1,n+1)]
        start=0
        while len(a)>1:
            Remove=(start+k-1)%len(a)
            a.pop(Remove)
            start=Remove
        return a[0]
           
        