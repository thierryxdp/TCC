def colchao(medidas, h, l):
    ''
    if medidas[1]>=h and medidas[2]<l:
        return True
    if medidas[2]>=h and medidas[1]<l:
        return True