def (quant_pecas):
    i=0
    while i < len(quant_pecas):
        if i+1 != quant_pecas[i]:
            return i
        else:
            return i+1