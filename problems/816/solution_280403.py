def maiores(lista,n):
    lista.append(n)
    lista.sort()
    posicao = lista.index(n)
    tamanho= len(lista)
  	lista_final = lista[posicao:tamanho]
    return lista_final