def colchao (medidas,H,L):
    '''insere uma lista com tamanhos A,B,C das dimensões do colchão, a 
    altura e a largura da porta, respectivamente, e retorna se o colchão
    passa pela porta ou não'''
    return medidas[0]<=L and medidas[1]<=H or medidas[0]<=H and medidas[1]<=L