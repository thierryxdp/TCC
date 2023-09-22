def maiores(l, n):
    m=[]
    i=0
    while i<len(l):
        if l[i]>n:
            m.append(l[1])
        i = i + 1
        
    return m