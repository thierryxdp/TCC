def faltante(lista):
    lista.sort()
    i = 0
    while i < len(lista):
        if lista[i]-1 not in lista and lista[i]-1 !=0:
            return lista[i]-1
        i +=1
    return lista[-1]+1