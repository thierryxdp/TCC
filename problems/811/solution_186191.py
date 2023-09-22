def colchao(lista,H,L):
    """função que retorna se um colchão passa ou não por uma porta
    list, int, int -> bool"""
    [a,b,c] = lista  
    if lista > H * L:
        return True
    else: 
        return False