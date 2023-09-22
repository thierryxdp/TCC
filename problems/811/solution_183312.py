def colchao(medidas,h,l):
    bc=medidas[0]
    hc=medidas[1]
    ac=medidas[2]
    if bc<=h and hc<=1 or bc<=h and ac<=1 or hc<=h and bc<=1 or hc<=h and ac<=1 or ac<=h and bc<=1 or ac<=h and hc<=1:
        return 'False'
    else:
        return 'True'