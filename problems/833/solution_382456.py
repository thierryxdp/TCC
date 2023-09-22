def conta_numero(numero,matriz):
    indice1=0
    contagem=0
    while indice1<len(matriz):
        indice2=0
        while indice2<len(matriz[0]):
            if matriz[indice1][indice2]==numero:
                contagem=contagem+1
            indice2=indice2+1
        indice1=indice1+1
    return contagem