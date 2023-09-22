def filtra_pares(tupla):
    
    total = tupla[0:3]
    
    if (tupla[0]%2 != 0):
        return (total - tupla[0])
    elif (tupla[1]%2 != 0):
        return (total - tupla[1])
    elif (tupla [2]%2 != 0):
        return (total - tupla[2])
    elif (tupla[3]%2 != 0):
        return (total - tupla[3])
    else:
        return 0