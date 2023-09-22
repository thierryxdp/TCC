def insere(lista,n):
    list.append(lista,n)
    list.sort(lista)
    return lista

def maiores(lista,n):
    for x in insere(lista,n)[:list.index(lista,n)]:
        list.remove(lista,x)
    return lista