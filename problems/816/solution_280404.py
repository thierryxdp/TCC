def maiores(lista,n):
    lista.append(n)
    lista.sort()
    posicao = lista.index(n)
    tamanho= len(lista)
  	lista = lista[posicao:tamanho]
    return lista