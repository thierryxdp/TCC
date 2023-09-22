def maiores(lista_numeros,n):
    """ dada a lista de numeros inteiros e um inteiro n, retorna outra lista que contenha todos os maiores que n"""
    list.append(lista_numeros,n)
    list.sort(lista_numeros)
    posicao= list.index(lista_numeros,n)+1
    return lista_numeros[posicao:]