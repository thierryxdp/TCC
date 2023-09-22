def posLetra(string,letra,num):
    acumulador=[]
    i=0
    while i<len(string):
        if letra in string[i]:
            acumulador=acumulador+[i,]
        i=i+1
    posicao=num-1
    if len(acumulador)<num:
        return -1
    else:
        return acumulador[posicao]