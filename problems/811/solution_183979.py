def colchao(medidas,H,L):
    """Dado como entrada a lista medidas, altura H e a largura L, retorna se o colchao consegue passar pela porta
    list,float,float==>bool"""
    if medidas[0]>H or (float(medidas[1])>H or (float(medidas[2])>H or (float(medidas[0])>L or (float(medidas[1])>L or (float(medidas[2])>L:
        return False
    else:
        True