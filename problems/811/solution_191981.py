def colchao(medidas,H,L):
    [A, B, C] = medidas
    """função que dado as medidas: A,B e C de um colchão e H e L de uma porta, retorna se é possível o colchão passar pela porta
    lista,int,int -> bool"""
    if medidas [0] <= L and medidas [1] <= H:
        return True 
    elif medidas [1] <= L and medidas [0] <= H:
        return True
    elif medidas [0] <= L and medidas [2] <= H:
        return True
    else:
        return False