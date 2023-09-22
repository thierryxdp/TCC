def colchao (medidas, h,l):
    if medidas[0] <= h and medidas[1] <= l:
        return 'true'
    if medidas[0] > h and medidas[1] > l:
        return 'false'