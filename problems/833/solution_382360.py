def conta_numero(numero,matriz):
    qtd=0
    c=0
    if len(matriz) == 1:
        for i in range(len(matriz)):
            if numero == matriz[i][c]:
                qtd += 1
                c += 1
        return qtd      
    else:
        for j in range(len(matriz)):
        return c