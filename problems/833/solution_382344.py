def conta_numero(numero,matriz):
    qtd=0
    c=0
    k=0
    for i in matriz[c]:
        c=c+1
        if numero == matriz[c][k]:
            k=k+1
            qtd=qtd+1
    return qtd