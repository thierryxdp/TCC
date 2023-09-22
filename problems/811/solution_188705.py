def colchao(medidas,H,L):
    """A função ao receber uma lista contendo os valores de "A", "B", "C"
    e os ints "H" e "L" retorna se é possível que o colchão atravesse a 
    porta.
    
    list, int, int ->bool"""
    
    if medidas[0] == min(medidas):
        novasmedidas = [medidas[1], medidas[2]]
        
    if medidas[1] == min(medidas):
        novasmedidas = [medidas[0], medidas[2]]
        
    if medidas[2] == min(medidas):
        novasmedidas = [medidas[0], medidas[1]]
        
    if min(novasmedidas) < L and max(novasmedidas) < H:
        return bool(1)
    
    if min(novasmedidas) < H and max(novasmedidas) < L:
        return bool(1)
    
    else:
        return bool(0)