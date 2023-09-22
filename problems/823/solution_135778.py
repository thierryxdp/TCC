def faltante(n):
    l=[0,1,2,3,4,5,6,7,8,9]
    i=0
    while i<len(n):
        if l[i] not in n:
            return l[i]
	return n[-1]+1