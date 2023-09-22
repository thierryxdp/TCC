def posLetra(s, l, n):
    o = 0
    for i in s:
        if i<n:
            return -1
        	o+=1
        if o == n:
            return s[o]
        	o+=1
    return -1