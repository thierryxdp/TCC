def colchao(medidas,h,l):
    """funcao que retorna se o colchao passa ou nao da porta de acordo com as medias, h e l"""
    altura_colchao = medidas[0]
    comprimento_colchao = medidas[1]
    largura_colchao = medidas[2]
    
    if (comprimento_colchao>h):
        if(largura_colchao>l):
            return False
        elif (largura_colchao<1):
            return True
        else:
            return True