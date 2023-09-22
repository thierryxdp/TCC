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
    media=sum(l)/len(l)
    m.append(maiores(l,media)
    return m