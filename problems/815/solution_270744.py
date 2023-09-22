def insere(lista_numero,n):
    '''
    Função que recebe uma lista de números e um número(n) 
    e o insere na posição correta.
    
    list, float -> list
    '''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero