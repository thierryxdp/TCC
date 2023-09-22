def colchao(medidas, H, L):
    """essa funcao"""
    
    area_porta = (H*L)
    area_paralelepipedo = (2*medidas[0]*medidas[1])+(2*medidas[1]*medidas[2])+(2*medidas[0]*medidas[2])
    return area_paralelepipedo < area_porta