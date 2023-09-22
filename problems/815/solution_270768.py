def insere(lista_numero, n):
    '''dada uma lista ordenada, insere um numero n e retorna
       uma outra lista ordenada com n no lugar correto'''
    lista = list(lista_numero)
    numero = list(n)
    return lista + numero