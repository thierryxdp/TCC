colchao(medidas,H,L):
    """Dadas uma lista das medidas de um colchão com a forma de um paralelepípedo,
    e as medidas da altura 'H' e largura 'L' de uma porta, a função calcula se esse colchão
    consegue passar ou não pela porta ao ser rotacionado. A função retorna 'True' caso o
    colchão passe e 'False', caso não passe;
    list, int, int --> boolean"""
    altura = min(medidas[0],medidas[1],medidas[2])
    comprimento = max(medidas[0],medidas[1],medidas[2])
    altura2 = medidas.index(altura)
    comprimento2 = medidas.index(comprimento)
    medidas[altura2] = medidas[comprimento2]
    largura = min(medidas[0],medidas[1],medidas[2])
    if (largura <= H) and (altura <= L):
        return True
    else:
        return False