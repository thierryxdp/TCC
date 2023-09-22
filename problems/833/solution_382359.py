def conta_numero(numero,matriz):
    qtd=0
    for i in range(0,len(matriz)):
        if numero == matriz[i]:
            qtd=qtd+1
    return qtd