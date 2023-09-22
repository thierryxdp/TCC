def colchao (medidas,H,L):
    '''Função com o objetivo de saber se um colchao entra pela
    porta'''
    if H >= medidas[0]:
        testealtura = 1
    else:
        testealtura = 0
    if H >= medidas[1]:
        testealtura += 1
    if H >= medidas[2]:
        testealtura += 1
    if L >= medidas[0]:
        testelargura = 1
    else:
        testelargura = 0
    if L >= medidas[1]:
        testeargura += 1
    if L >= medidas[2]:
        testelargura += 1
    if (testelargura >= 2 and testealtura >=1) or (testeatura >=2 and testealtura >=1):
        return ('True')