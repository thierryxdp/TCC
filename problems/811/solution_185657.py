def colchao(medidas,H,L):
    '''calcula se o colchao com as medidas dadas passa pela porta com as medidas dadas com um de seus lados
    paralelos ao chão.
    list, int|float, int|float -> bool'''
    lado1 = medidas[0]
    lado2 = medidas[1]
    lado3 = medidas[2]
    if   H >= lado2 or H >= lado3 :
        return True
    if   L >= lado2 or L >= lado3 :
        return True
    else:
        return False