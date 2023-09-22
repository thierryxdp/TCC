def filtra_pares(x):
    
    lis = []
    
    for i in range(len(x)):
        if x[i] % 2 == 0:
            tuple(lis.append(x[i]))
            
            return tuple(lis)