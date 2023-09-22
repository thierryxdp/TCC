def busca(a,m):
    x=[]
    i=0
    for c in m:
        if len(m[2])==a:
            m=m[i]
            x+=[m[0],m[1],m[3]]
            i+=1
    return x