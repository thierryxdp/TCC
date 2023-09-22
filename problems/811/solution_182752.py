from math import sqrt
def colchao(medidas,h,l):
    '''Essa função recebe uma lista com as medidas de um colchão
    e dois números correspondentes às dimensões da porta da casa, assim calcula se um determinado
    colchão comprado poderá ou não passar pela porta;
    LIST, FLOAT, FLOAT -> BOOL'''
    max(medidas[0],medidas[1],medidas[2]) = ccolc
    min(medidas[0],medidas[1],medidas[2]) = gcolc
    (medidas[0]+medidas[1]+medidas[2])-(ccolc+gcolc) =lcolc
    if (lcol < h and gcolc < l):
        return True
    else:
        return False