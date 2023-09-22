def insere(lista,n):
    list.append(lista,n)
    list.sort(lista)
    return lista

def maiores(lista,n):
    if n in lista:
        list.sort(lista)
        indice=list.index(lista,n)
        return lista[indice+1:]
    else:
        insere(lista,n)
        indice=list.index(lista,n)
        return lista[indice + 1:]