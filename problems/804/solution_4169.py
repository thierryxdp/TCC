def filtra_pares(tupla):
    
    lis = []
    
    for tupla[0] in range(len(tupla)):
        if tupla[0] % 2 == 0:
            lis.append(tupla[0])
            
            return tuple(lis)