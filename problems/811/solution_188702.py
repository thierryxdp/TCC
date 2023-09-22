def colchao(medidas,H,L):
    """A função ao receber uma lista contendo os valores de "A", "B", "C"
    e os ints "H" e "L" retorna se é possível que o colchão atravesse a 
    porta.
    
    list, int, int ->bool"""
    
    del(min(medidas))
    
    if max(medidas) < H and min(medidas) < L:
        return bool(1)
    
    if max(medidas) < L and min(medidas) < H:
        return bool(1)
    
    else:
        return bool(0)