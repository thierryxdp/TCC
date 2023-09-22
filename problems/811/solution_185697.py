def colchao_novo (medidas, H, L):
    """Função que retorna se será possivel ou não passar com um colchão por uma porta com medidas H e L"""
    alt_colchao = medidas [0]
    comp_colchao = medidas [1]
    larg_colchao = medidas [2]
    
    if (comp_colchao>H):
        if (larg_colchao>L):
            return False
    elif (larg_colchao<L):
        return True
    else:
        return True