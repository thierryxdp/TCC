def posLetra(s,l,n):
    i=0
    lista=[]
    while i<len(s):
        if s[i]==l:
            i+=1
            lista.append(i)
            i+=1
        else:
            i+=1
    if n==c:
        return lista[-1]
    else:
        return -1