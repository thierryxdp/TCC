def maiores(lista,n):
    lista.append(n)
    lista.sort()
    comeco_nova_lista = lista.index(n)
    return lista[comeco_nova_lista+1:]