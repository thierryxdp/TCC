def insere(lista_numero, n):
    '''esta e a funçao insere que dada uma lista ordenada e um numero inteiro que inclue na posiçao correta'''
    '''list, int -->list'''
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero