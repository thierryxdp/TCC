def filtra_pares(tupla):
    
    listatupla = (tupla)

    for n in tupla:
        if n % 2 == 0:
            listatupla.append(n)
    
    tupla = tuple(listatupla)
    
    return listatupla