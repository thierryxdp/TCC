def colchao(medidas,h,l):
    """função que calcula a dimensão de um colcção em centimetros e retorna se ele passa ou não da porta da casa do joão
    list -> bool"""
    a=medidas[0]
    b=medidas[1]
    if (b<=h and a<=l) or (b<=l and a<=h):
        return True
    else:
        return False