def filtra_pares(n):
    new_list = []
    for i in range(len(n)):
        if n[i]/2 == int(n[i]/2):
            new_list.append(n[i])
    
    return tuple(new_list)