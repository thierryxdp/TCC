def colchao(medidas,h,l):
    if medidas[0]<=l and medidas[1]<=l and medidas[2]<=l:
        return True
    if medidas[0]<=h and medidas[1]<=h and medidas[2]<=h:
        return True
    if medidas[0]<=h and medidas[1]<=l:
        return True
    if medidas[0]<=h and medidas[2]<=l:
        return True
    if medidas[1]<=h and medidas[2]<=l:
        return True
    if medidas[1]<=h and medidas[0]<=l:
        return True
    if medidas[2]<=h and medidas[0]<=l:
        return True
    if medidas[2]<=h and medidas[1]<=l:
        return True
    else:
        return False