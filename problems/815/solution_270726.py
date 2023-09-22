def insere(lista_numero, n):
    '''Retorna uma função que dada uma lista ordenada inclui n na posição correta
    str,int-->str'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero