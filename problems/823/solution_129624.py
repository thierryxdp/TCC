def faltante(lista):
    i=0
    c=1
    lista.sort()
    lista2=[]
    lista3=[]
    while i<len(lista):
        if lista[i]==c:
            i+=1
            c+=1
        else:
            lista2.append(c)
            i+=1
            c+=1
    if lista2==lista3:
        return lista[-1]+1
    elif lista2!=lista3:
        return lista2[0]