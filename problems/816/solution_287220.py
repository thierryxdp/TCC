def menores(lista_numeros, n):
    '''dada uma lista de numeros inteiros e um
numero inteiro n, retorna outra lista, que contenha todos os ńumeros da
lista original maiores que n.'''
    #list > list
    #adiciona n a lista
    lista_numeros.append(n)
    #põe a lista em ordem crescente
    lista_numeros.sort()
    #acha a primeira ocorrencia de n
    indice = lista_numeros.index(n)
    #deleta tudo a partir desse indice
    del lista_numeros[indice:]
    #retorna a lista
    return lista_numeros