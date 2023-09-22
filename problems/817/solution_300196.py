def maiores(l, n):
    m=[]
    i=0
    while i<len(l):
        if l[i]>=n:
            m.append(l[i])
    	i = i + 1
        
    return sorted(m,key=int)

def acima_da_media(l):
    m=[]
    m.append(maiores(l,5))
    return m