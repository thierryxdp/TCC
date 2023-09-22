def posLetra(s,l,n):
    i=0
    lista=[]
    while i<len(s):
        if s[i]==l:
            lista.append(i)
            i+=1
        else:
            i+=1
    if lista.count()==n:
        return lista[-1]
    elif lista.count()>n:
        return lista[n]
    else:
        return -1