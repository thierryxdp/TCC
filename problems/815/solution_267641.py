def insere(lista_numero, n):
    """ Função que dada uma lista ordenada de números inteiros e um número inteiro n, 
    inclua n na posição correta, ou seja, que a lista continue ordenada"""
    lista_numero.append(n)
    lista_numero.sort()

#    return list.sort(lista_numero)
    return lista_numero