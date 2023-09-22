def maiores(m,n):
    list.append(m,n)
    list.sort(m)
    a=list.index(m,n)
    s=m[a+1:]
    return s

def acima_da_media(q):
    w=sum(q)/len(q)
    if w in q:
        e=maiores(q,w)
        return maiores[1:]
    else:
    	return maiores(q,w)