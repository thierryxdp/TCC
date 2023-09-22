def filtra_pares(n):
    n_list = list(n)
    new_list = []
    for i in n_list:
        if i/2 == 0:
            new_list.append(i)
    
    return tuple(new_list)