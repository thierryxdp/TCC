def conta_numero(numero,matriz):
    qtd=0
    c=0
    for i in range(0,len(matriz)):
        c=c+1
        if numero == matriz[c][i]:
            qtd=qtd+1
    return qtd