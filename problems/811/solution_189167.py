def colchao(medidas,h,l):
    bc = medidas[0]
    hc = medidas[1]
    pc = medidas[2]
    if  bc <= h and hc <= l or bc <= h and pc <= l or hc <= h and bc <= l or hc <= h and pc <= l or pc <= h and bc <= l or pc <= h and hc <= l :
        return True
    else:
        return False