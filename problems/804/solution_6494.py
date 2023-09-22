def filtra_pares(x,y,z,w):
    """analisa os numeros e retorna somente os que sao par"""
    
    restox = x%2
    restoy = y%2    
    restoz = z%2    
    restow = w%2 
    
    if restox == 0:
        if restoy == 0:
            if restoz == 0:
                if restow == 0:
                    return x, y, z, w
                elif restox > 0:
                    if restoy == 0:
                        if restoz == 0:
                            if restow == 0:
                                return y, z, w