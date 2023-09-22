def colchao(medidas,h,l):
    ''''''
    if min(medidas[1],medidas[2]) < h or l:
        return medidas[1]
    else:
        return False