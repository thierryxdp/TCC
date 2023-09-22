def colchao(medidas,h,l):
    ''
    if h<=medidas[1]>=l:
        return False
    if h<=medidas[2]>=l:
        return False
    if h<=medidas[2]>=l and h<=medidas[1]>=l:
        return False
    else:
        return True