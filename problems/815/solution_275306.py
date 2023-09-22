def insere(lista_numero, n):
    '''dada uma lista ordenada (crescente) de ńumeros inteiros e um ńumero inteiro n, inclua n na posi ̧c ̃ao
correta, ou seja, de tal maneira que a lista continue ordenada.'''
    #list > list
    #adiciona o numero n ao fim da lista
    lista_numero.append(n)
    #ordena a lista em ordem crescente
    lista_numero.sort()
    #retorna a lista ordenada
    return lista_numero