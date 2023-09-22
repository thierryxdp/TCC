def faltante(n):
    ll=n[-1]+1
    l=n+ll
    i=0
    while i<len(n):
        if l[i] not in n:
        
            return l[i]
        i+=1
	return ll