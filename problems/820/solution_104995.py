def posLetra(s, l, n):
    o = 0
    for i in s:
        if s[i]<n:
            return -1
        	o+=1
        if o == n:
            return s[i]
        	o+=1
    return -1