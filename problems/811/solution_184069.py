def colchao(medias,H,L):
    """Funcao para saber se um colchao passa pela porta
    entradas: lixt [float, float, float], int, int;
    saidas:bool"""
    
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    
    maior = max (L,H)
    menor = min (L,H)
    
    if (B> maior):
        return False
    
    elif (B<= maior) and (A> menor):
        return False
    
    else:
        return True