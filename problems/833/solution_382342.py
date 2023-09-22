def conta_numero(numero,matriz):
    qtd=0
    c=0
    for i in matriz[c]:
        if numero == matriz[c][i]:
            qtd=qtd+1
    return qtd