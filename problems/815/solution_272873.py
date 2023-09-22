def insere(lista_numero,n):
    '''
    função que recebe uma lista ordenada e um um número inteiro n (entre aspas), e inclui n na posição correta para a lista continuar ordenada;
    list, int -> list
    '''
    lista_numero[0:0] = [n]
    list.sort(lista_numero)
    return lista_numero