def maiores(lista,n):
    lista.append(n)
    lista.sort()
    posicao = lista.index(n)
    tamanho= len(lista)
    return lista[posicao:tamanho]