def conta_numero(numero,matriz):
    quant=0
    total=0
    for n in matriz:
        n=matriz[quant].count(numero)
        quant=quant+1
        total=total+n
    return total