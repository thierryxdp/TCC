def conta_numero(numero,matriz):
    cont=0
    n_linhas=len(matriz)
    n_cols=len(matriz[0])
    for i in range(n_linhas):
        for i in range(n_cols):
            if numero == matriz[i][j]:
                cont+=1
    return cont