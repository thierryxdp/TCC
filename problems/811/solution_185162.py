def colchao(medidas,h,l):
    """..."""
    altura_colchao = medidas[0]
    comprimento_colchao = medidas[1]
    largura_colchao = medidas[2]
    
    if (largura_colchao<l):
            return True
        elif (comprimento_colchao>h):
            if (largura_colchao>l):
                return False
            else:
                return True