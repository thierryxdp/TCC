def insere(lista_numero,n):
    '''funcao que insere um numero ja ordenado em uma lista. list-> list'''
    lista_numero.append(n) 
    lista_numero.sort()
    return lista_numero