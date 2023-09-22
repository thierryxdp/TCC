def colchao(medidas, H, L):
    '''função que recebe as medidas do colchão e da porta e retorna
    True caso o colchão passe pela porta e False caso não'''
    if (medidas[0] or medidas[1] or medidas[2] > H) and (medidas[0] or medidas[1] or medidas[2] > L):
        return False
    else:
        return True