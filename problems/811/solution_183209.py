def colchao(medidas,h,l):
    '''funcao que verifica se o colchao a partir de suas dimensoes passara ou nao da porta'''
    bc = medidas[0]
    hc = medidas[1]
    pc = medidas[2]
    if (bc <= h and hc <= 1) or (bc <= h and pc <= 1) or (hc <= h and bc <= 1) or (hc <=h and pc <=1) or (pc <=h and bc <= 1) or (pc <= h and hc <= 1):
        return 'true'
    else:
        return 'false'