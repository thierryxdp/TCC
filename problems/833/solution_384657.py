def conta_numero(numero, matriz):
    contagem=0
    for i in matriz:
        w=list.count(i,numero)
        contagem=contagem+w
    return contagem