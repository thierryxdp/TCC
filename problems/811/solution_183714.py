def colchao(medidas, H, L):
    """essa funcao"""
    
    area_porta = (H*L)
    area_paralelepipedo = medidas[1]*medidas[2]
    if area_paralelepipedo <= area_porta:
        return True
    else:
        return False