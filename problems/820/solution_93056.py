def posLetra(s,l,n):
    i=0
    lista=[]
    while i<len(s):
        if s[i]==l:
            lista.append(i)
            i+=1
        else:
            i+=1
    if len(lista)==n:
        return lista[-1]
    elif len(lista)>n:
        return lista[(n-1)]
    else:
        return -1