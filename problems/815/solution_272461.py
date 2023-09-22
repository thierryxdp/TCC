def insere(lista_numero,n):
    '''Funcao que dada uma lsita ordenada de numeros inteiros e um numeor inteiro n, inclui n na
    posicao correta mantendo a lista ordenada
    list,int->list
    '''
    lista_numero.append(n)
    return lista_numero.sort()