def colchao(dimensoes,h,l):
    bc = dimensoes[0]
    hc = dimensoes[1]
    pc = dimensoes[2]
    if bc <= h and hc <= 1 or bc <= h and pc <= 1 or hc <= h and bc <= 1 or hc <= h and pc <= 1 or pc <= h and bc <= 1 or pc <= h and hc <= 1:
        return 'True'
    else:
        return 'False'