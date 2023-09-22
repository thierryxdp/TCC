def repetidos(n):
    quant=0
    i=0
    while i<len(n):
        if quant[i] in n:
            quant = quant +1
            i=i+1
            return quant