def filtra_pares(x):
    
    lis = []
    
    for x[0] in range(len(x)):
        if x[x[0]] % 2 == 0:
            lis.append(x[x[0]])
            
            return tuple(lis)