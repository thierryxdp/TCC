def colchao(medidas,h,l):
    """Função que recebe uma lista contendo as medidas de um colchão, além da altura e largura de uma porta e retorna se seria possivel passar com o colchão por esta porta."""
    """lista, int->boolean"""
    if medidas[0]<h and medidas[1]<l:
        return True
    elif medidas[0]<h and medidas[2]<l:
        return True
    elif medidas[1]<h and medidas[2]<l:
        return True
    elif medidas[1]<h and medidas[0]<l:
        return True
    elif medidas[2]<h and medidas[0]<l:
        return True
    elif medidas[2]<h and medidas[1]<l:
        return True
    else:
        return False