def insere(lista_numero,n):
    '''Dada uma lista com números e um número n. Retorna uma lista com o número n inserido em ordem crescente
    list, float -> list'''
    lista_numero.append(n)
    lista_numero.sort()
    
    return lista_numero