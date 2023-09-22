def colchao(medidas,H,L):
    '''scmsczx msjfks:
    lista, int, int -> bool'''
    altura_colchao = medidas[0]
    comprimento_colchao = medidas[1]
    largura_colchao = medidas[2]
    if (comprimento_colchao>H):
        return False
    elif (largura_colchao<1):
        return True
    else:
        return True