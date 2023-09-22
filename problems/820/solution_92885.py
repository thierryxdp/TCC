def posLetra(s,l,n):
    i=0
    lista=[]
    c=0
    while i<len(s):
        if s[i]==l:
            lista.append(i)
            i+=1
            c+=1
        else:
            i+=1
    if n==lista[i]:
        return lista[i-1]
    else:
        return -1