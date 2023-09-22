def conta_numero(numero,matriz):
    contagem=0
    elementos=0
    for elementos in matriz[[0]]:
        if (elementos==numero):
            contagem+=1
    return contagem