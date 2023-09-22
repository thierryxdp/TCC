def filtra_pares(x):
    """Recebe quatro inteiros e retorna apenas os pares.
    int int int int -> int pares"""
    
    pares = []
    
    for a in range(len(x)):
        if x[a] % 2 == 0:
            pares.append(x[a])
            
            return x(pares)