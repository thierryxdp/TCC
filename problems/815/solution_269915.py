def insere(lista_numero,n):
    '''Funcao que dada uma lista ordenada de numeros inteiros e um numero
    inteiro n, retorna uma lista ordenada com o n na posicao correta
    list, int -> list'''
    insercao = list.append(lista_numero,n)
    ordem = list.sort(lista_numero)
    return lista_numero