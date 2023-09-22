def insere(lista_numero,n):
    '''Inclui um número inteiro n em uma lista de inteiros crecentes
    list , int -> list'''
    list.append(lista_numero,n)
    lista_numero.sort(reverse=False)
    
    return lista_numero