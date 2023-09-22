def colchao(medidas,H,L):
    """list,int,int -> bool"""
    """ recebe as medidas do objeto e retorna se ele passa ou não pela porta""""
    
    H1,H2,H3 = medidas[0] <= H, medidas[1] <= H, medidas[2] <= H
    L1,L2,L3 = medidas[0] <= L, medidas[1] <= L, medidas[2] <= L
    
    M1,M2,M3 = H1 and (L2 or L3), H2 and (L1 or L3), H3 and (L1 or L3)
    
    return M1 or M2 or M3