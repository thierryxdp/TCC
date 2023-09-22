def insere(lista_numero,n):
    ''' Função que recebe uma lista(lista_numero) e um numero(n)
        inteiro, e depois inclui o (n) na posição correta dentro
        da lista, da forma que, os números dentro da lista
        fiquem ordenados. 
        : param lista_numero: list
        : param n: int
        : return: list
    '''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero