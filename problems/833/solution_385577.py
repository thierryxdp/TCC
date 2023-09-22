def conta_numero(numero,matriz):
    contagem=0
    elementos=0
    for elementos in range(len(matriz)):
        if (elementos==numero):
            contagem+=1
    return contagem