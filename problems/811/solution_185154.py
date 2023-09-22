def colchao(medidas,h,l):
    """..."""
    altura_colchao = medidas[0]
    comprimento_colchao = medidas[1]
    largura_colchao = medidas[2]
    
    if (comprimento_colchao>h):
        if (largura_colchao>l):
            return False
        elif (largura_colchao<l):
            return True
        else:
            return True