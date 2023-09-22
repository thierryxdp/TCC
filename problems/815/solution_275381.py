def insere(lista_numero,n):
    '''recebe uma lista ordenada do maior para o menor
    e insere um numero n na posicao correta seguindo a 
    ordem da lista
    list, int -> list'''
    
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero