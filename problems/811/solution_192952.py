def colchao(medidas, H,L):
    '''funcao define se colchao passa pela porta de acordo com as medidas do colchao. list, float, float --> bool'''
    if medidas[1] <= H:
        return True
    if medidas[1] <= L:
        return True
    if medidas[2] <= H:
        return True
    if medidas[2] <= L:
        return True
    else:
        return False