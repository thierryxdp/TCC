def conta_numero(numero,matriz):
    qtd=0
    c=0
    for i in range(0,len(matriz)):
        if numero == matriz[i]:
            c=c+1
            qtd=qtd+1
    return qtd