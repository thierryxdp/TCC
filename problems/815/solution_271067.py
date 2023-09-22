def insere(lista_numero,n):
    '''Dada uma lista ordenada crescente de numeros inteiros
    e um numero inteiro n, incluindo n na posicao correta para
    que a lista continue ordenada
    list,int -> list'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero