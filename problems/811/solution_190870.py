def colchao(medidas,h,l):
    hc=medidas[1]
    lc=medidas[2]
    if hc>h and lc>l:
        return False
    else:
        return True