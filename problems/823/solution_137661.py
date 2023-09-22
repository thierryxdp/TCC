def faltante(quant):
    i=0
    while i < len(quant):
        if quant[i] != i:
            return i