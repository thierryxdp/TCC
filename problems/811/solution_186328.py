def colchao(medidas,h,l):
    if medidas[2]>h and medidas[1]>l:
        return false
    if medidas[0]>medidas[1]:
        return false
    else:
        return true