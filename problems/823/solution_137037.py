def faltante (lista):
    i = 0 
    lista.sort()
    while i< len(lista):
        print(i, lista[i] - 1)
        if lista [i] - 1 in lista:
            if lista[i]-1 ==0:
                continue
            return lista[i]-1
        i +=1
    return lista[-1] + 1