def colchao(medidas,H,L):
    """Função de medidas é uma lista com os tamanhos inteiros A,B e C, e H e L são os tamanhos inteiros da altura e largura da porta, respectivamente,
    lista,int,int --> float"""
    A = medidas[0]
    B = medidas[1]
    
    if (B <= H and A <= L) or (B <= L and A <= H):
        return True 
    else:
        return False