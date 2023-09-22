def posLetra(s,l,n):
    if 0 < n <= s.count(1):
        
        i = 0
        while n > 0:
            i = s.find(l, i)
            n-=1
        return i