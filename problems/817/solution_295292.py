def maiores(lista:list, n:int)->list:
    lista.append(n)
    lista.sort()
    aux = lista.index(n)
    return lista[aux+1:]

def acima_da_media(lista:list)->list:
    n = sum(lista)//len(lista)
    return maiores(lista, n)