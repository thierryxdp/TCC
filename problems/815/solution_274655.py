def insere(lista_numero,n):
    '''
    Função que dada uma lista ordenada crescente de números inteiros e um número
    inteiro n, inclui 'n' na posição correta de maneira que ela continue ordenada
    list-> list
    '''
    lista_numero.insert(n)
    lista_numero=list.sort(lista_numero)
    
    return list.sort(lista_numero)