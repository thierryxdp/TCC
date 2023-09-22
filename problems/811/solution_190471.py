def colchao(medidas,h,l):
    ''
    if h<=medidas[1]>=l and h>=medidas[2]<=l:
        return True
    if h<=medidas[1]>=l and h>=medidas[2]<=l:
        return True
    if h<=medidas[2]>=l and h<=medidas[1]>=l:
        return False
    else:
        return True