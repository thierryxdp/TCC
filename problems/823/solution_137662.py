def faltante(quant):
    i=1
    while i < len(quant):
        if quant[i] != i:
            return i