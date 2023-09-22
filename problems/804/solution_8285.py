def filtra_pares(n):
    new_list = []
    for i in range(n):
        if n[i]/2 == 0:
            new_list.append(n[i])
    
    return tuple(new_list)