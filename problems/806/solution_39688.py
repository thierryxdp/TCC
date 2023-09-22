#Start your python function here
def colisao(ret1x1,ret1y1,ret1x2,ret1y2,ret2x1,ret2y1,ret2x2,ret2y2):
    """Testa se os retangulos paralelos aos eixos com
    coordenadas dadas se colidem ou não.
    Entradas: 8 ints
    Saída: bool"""
    
    #Comentário: é melhor detectar não-colisão! são 4 casos:
    #lado dir. de ret1 à esq. do lado esq. de ret2
    #ret2 à esquerda de ret1
    #ret1 abaixo de ret2
    #ret2 abaixo de ret1 
    
    if max(ret1x1,ret1x2) < min(ret2x1,ret2x2) or max(ret2x1,ret2x2) < min(ret1x1,ret1x2) or max(ret1y1,ret1y2) < min(ret2y1,ret2y2) or max(ret2y1,ret2y2) < min(ret1y1,ret1y2):
        return False
    else:
        return True