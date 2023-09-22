def maiores(lista:list, n:int)->list:
    lista.append(n)
    lista.sort()
    aux = lista.index(n)
    return lista[aux+1:]