def repetidos (lista):
    quant= 0
    c= 0
    c1= 1
    while c and c1 in lista:
        if lista[c] == lista[c1]:
            quant=quant+1
        c=c+1
        c1=c1+1
    return quant