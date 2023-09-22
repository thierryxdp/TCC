def insere(lista_numero, n):
    '''dada uma lista ordenada, insere um numero n e retorna
       uma outra lista ordenada com n no lugar correto'''
    lista = (lista_numero)
    numeros = (n)
    resultado = [lista,numeros]
    return list.extend(lista,numeros)