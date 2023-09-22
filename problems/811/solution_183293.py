def colchao(medidas,h,l):
    bc=medidas[0]
    hc=medidas[1]
    pc=medidas[2]
    if bc<=h and hc<=1 or bc<=h and pc<=1 or hc<=h and pc<=1 or pc<=h and bc<=1 or pc<=h and hc<=1:
        return 'True'
    else:
        return 'False'