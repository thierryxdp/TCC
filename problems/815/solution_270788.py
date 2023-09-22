def insere(lista_numero, n):
    '''dada uma lista ordenada, insere um numero n e retorna
       uma outra lista ordenada com n no lugar correto'''
    lista = (lista_numero)
    lista[1:1] = [n]
    return lista