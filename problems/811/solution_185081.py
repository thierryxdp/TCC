def colchao(medidas,H,L):
    """Função que retorna as medidas de um colchão int->int"""
    if L>medidas and H>medidas:
        return True
    elif L>=medidas and H>=medidas:
        return True
    else:
        return False