def maiores(lista,n):
    nova_lista=lista + [n]
    nova_lista.sort()
    idx=nova_lista.index(n)
    quantidade=nova_lista.count(n)
    return nova_lista[idx+quantidade:]