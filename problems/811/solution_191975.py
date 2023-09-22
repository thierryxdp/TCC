def colchao(medidas,H,L):
    medidas = [A,B,C]
    """função que dado as medidas: A,B e C de um colchão e H e L de uma porta, retorna se é possível o colchão passar pela porta
    lista,int,int -> bool"""
    if medidas [0] <= L and medidas [1] <= H:
        result = True 
    elif medidas [1] <= L and medidas [0] <= H:
        result = True
    elif medidas [0] <= L and medidas [2] <= H:
        result = True
        else:
        result = False