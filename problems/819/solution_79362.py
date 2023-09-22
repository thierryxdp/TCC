def filtraMultiplos(lista, n):
    '''Esta função retorna uma lista contendo alguns 
    números da lista que foi fornecida pelo usuário
    que forem divisíveis por n.
    Instruções: Forneça como entrada umalista entre [] e um inteiro.
    list, int -> list'''
    n_termo = 0
    new_list = ()
    while n_termo+1 < len(lista):
        if n_termo % n == 0:
        	x = lista[n_termo]
        	list.append(new_list,x)
        	n_termo = n_termo + 1
        else:
            n_termo = n_termo + 1
    return new_list