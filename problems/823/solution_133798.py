def faltante(pecas: list) -> int:
    falta = 0
    
    for i in range(1, len(pecas) + 2):
        if (i not in pecas):
            falta = i
            
    return falta