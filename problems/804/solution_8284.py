def filtra_pares(n):
    n_list = list(n)
    new_list = []
    for i in range(len(n_list)):
        if int(n_list[i])/2 == 0:
            new_list.append(n_list[i])
    
    return tuple(new_list)