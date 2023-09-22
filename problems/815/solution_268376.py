def insere (lista_numero, n):
    ''' funcao que dado uma lista ordenada e um numero n, inserir este numero n na posição que mantenha a funcao na ordem'''
    ''' list, int -> list '''
    for i, elemento in enumerate(lista_numero):
        if n < elemento:
            lista_numero.insert(i, n)
            return lista_numero