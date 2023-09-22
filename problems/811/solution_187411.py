def colchao(medidas,h,l):
    ''''''
    if medidas[1]<=h:
        return True
    if medidas[1]>=h and medidas[2]<l:
        return True
    else:
        return False