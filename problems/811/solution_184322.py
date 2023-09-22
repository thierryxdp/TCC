def colchao(medidas, H, L):
    '''função que recebe as medidas do colchão e da porta e retorna
    True caso o colchão passe pela porta e False caso não'''
    if medidas[1] or medidas[2] <= H or medidas[1] or medidas[2] <= L:
        return True
    else:
        return False