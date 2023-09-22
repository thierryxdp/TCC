def faltante(lista):
    i=0
    lista.sort()
    lista2=[]
    lista3=[]
    while i<=len(lista):
        if lista[i]==(i+1):
            i+=1
        else:
            lista2.append(i+1)
            i+=1
    if lista2==lista3:
        return lista[-1]+1
    elif lista2!=lista3:
        return lista2[0]