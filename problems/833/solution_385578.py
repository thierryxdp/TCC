def conta_numero(numero,matriz):
    contagem=0
    elementos=0
    for elementos in range(matriz):
        if (elementos==numero):
            contagem+=1
    return contagem