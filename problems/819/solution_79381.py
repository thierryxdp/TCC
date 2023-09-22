def filtraMultiplos(lista, n):
    '''Esta função retorna uma lista contendo alguns 
    números da lista que foi fornecida pelo usuário
    que forem divisíveis por n.
    Instruções: Forneça como entrada umalista entre [] e um inteiro.
    list, int -> list'''
    n_termo = 0
    k = 0
    new_list = ()
    x = len(lista)
    while n_termo < x:
        if lista[k] % n == 0:
            list.append(new_list,lista[k])
    	n_termo = n_termo + 1
    return new_list