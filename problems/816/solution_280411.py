def maiores(lista,n):
    """list, int --> list
    adiciona o elemento n ao final da lista, ordena-se a lista em ordem crescente.
    procura-se o valor adicionado e sua posicao.
    retorna o valor da posicao do elemento +1 (exclui ele) e os elemetos maiores que ele"""
    lista.append(n)
    lista.sort()
    posicao = lista.index(n)
    tamanho= len(lista)
    return lista[posicao+1:tamanho]