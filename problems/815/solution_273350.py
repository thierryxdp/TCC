def insere(lista_numero,n):
    '''Esta e a funcao que dada uma lista ordenada crescente
    de numeros inteiros e um numero inteiro n, inclue n na 
    posicao correta ordenada da lista
    int, int -> int'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista