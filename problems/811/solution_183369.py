def colchao(medidas,H,L):
    '''Retorna se e possivel a passagem de um colchao por uma porta com altura
    H e largura L.
    Entrada: list, int, int
    Saida: Bool
    
    Parameters:
    medidas: lista com as medidas do colchao;
    H: Altura da porta;
    L: Largura da porta;
    '''
    
    A,B,C = medidas
    
    if (A <= L and B <= H) or (A <= L and C <= H) or (B <= L and C <= H) or (B <= L and A <= H):
        return True
    else:
        return False