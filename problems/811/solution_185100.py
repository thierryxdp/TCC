def colchao(medidas,H,L):
    """Função que retorna as medidas de um colchão int->int"""
    a,b,c=medidas[:]
    if L>a and H>b:
        return True
    elif L>a and H>c:
        return True
    else:
        return False