def colchao_novo (medidas,H,L):
    """Função que retorna se é possivel passar com um colchão por uma porta, tendo em vista as medidas, altura e larguras deles"""
    alt_colchao = medidas [0]
    comp_colchao = medidas [1]
    larg_colchao = medidas [2]
    if (comp_colchao>H):
        if (larg_colchao>1):
        return False
    elif (larg_colchao<1):
        return True
    else:
        return True