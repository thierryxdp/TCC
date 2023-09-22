def colchao(medidas,H,L):
    '''calcula se o colchao consegue passar ou nao pela porta
    lista,int,int-> bool'''
    if medidas[1]<=H:
        return True
    if medidas[1]<=L:
        return True
    else:
        return False