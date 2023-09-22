def repetidos(ls):
    ft=ls[1:]
    r =[]
    for i in range(len(ft)):
    
        if ls[i]==ft[i]:
             r.append((i,i+1))
    return len(r)