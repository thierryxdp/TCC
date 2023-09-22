def maiores(lista_de_numeros_inteiros,n):
    '''Função que calcula o maior de uma lista de número inteiro e um numero inteiro n e retorna uma outra lista.
       list, int ---> list'''
    list.reverse(lista_de_numeros_inteiros)
    lista_de_numeros_inteiros = list.insert(lista_de_numeros_inteiros,n)
    list.reverse(lista_de_numeros_inteiros)
    primeira_posicao = list.index(lista_de_numeros_inteiros,n)
    return lista_de_numeros_inteiros[:primeira_posicao]