def colchao(medidas,h,l):
    """função faz o calculo para saber se o colchao passa, usei uma variavel auxiliar pra inverter os valores e deixar mais facil o calculo"""
    aux = 0
    if (medidas[0] > medidas[1]):
        aux = medidas[0]
        medidas[0] = medidas[1]
        medidas[1] = aux
    if (medidas[1] > medidas[2]):
        aux = medidas[1]
        medidas[1] = medidas[2] 
        medidas[2] = aux
    if (medidas[0] > medidas[1]):
        aux = medidas[0] 
        medidas[0] = medidas[1]
        medidas[1] = aux
    if (l > h):
        aux = h
        h = l
        l = aux
    if (h >= medidas[1]):
        return True
    else:
        return False