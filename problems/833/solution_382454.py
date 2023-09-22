def conta_numero(numero,matriz):
    indice1=0
    contagem=0
    while indice1<len(matriz):
        for elemento in len(matriz[0]):
            if elemento=numero:
                contagem=contagem+1
        indice1=indice1+1
    return contagem