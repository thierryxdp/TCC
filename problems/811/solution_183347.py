def colchao(dimensoes,H,L):
    """funcao que retorna se um colchao de dadas dimensoes passa por uma porta de dimensoes H e L
    list,int,int -> bool"""
    
    if dimensoes [0] <= H and dimensoes [1] <= L or dimensoes [0] <= H and dimensoes [2] <= L or dimensoes [1] <= H and dimensoes [2] <= L or dimensoes [2] <= H and dimensoes [1] <= L or dimensoes [0] <= L and dimensoes [1] <= H or dimensoes [0] <= L and dimensoes [2] <= H:
        return True
    else:
        return False