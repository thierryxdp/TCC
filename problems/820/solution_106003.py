def posLetra(s,L,n):
    m=0
    for i in "abcdefghijklmonpqrstuvwxyz":
        if s[L]==L:
            m+=1
        if m==n:
        	return i
    return -1