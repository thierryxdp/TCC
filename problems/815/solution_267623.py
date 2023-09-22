def insere(lista_numero,n):
    '''Função recebe uma lista ordenada e um numero inteiro qualquer e inclui o mesmo na lista de forma a manter sua organização.
    lista, int -> lista'''
    
    lista_numero.append(n)
    lista_numero.sort()

    return lista_numero