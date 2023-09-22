def faltante(l):
    lista1=l[1:]
    i=0
    while i<len(l) :
        if lista1[i]!=l[i]:
            i+=1
            return l[i]+1