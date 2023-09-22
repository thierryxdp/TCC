def conta_numero(numero,matriz):
    quant=0
    for l in matriz:
        for x in l:
            if numero==x:
                quant=quant+1
                
    return quant