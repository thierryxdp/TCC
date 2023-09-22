def maiores(m,n):
    list.append(m,n)
    list.sort(m)
    if n in m:
        a=list.index(m,n)
    	s=m[a+2:]
    	return s
    else:
    	a=list.index(m,n)
    	s=m[a+1:]
    	return s

def acima_da_media(q):
    w=sum(q)/len(q)
    if w in q:
        
    return maiores(q,w)