def conta_numero(numero,matriz):
    contador=0
    indice=0
    linhas=len(matriz)
    colunas=len(matriz[indice])
    while indice<linhas:
        for elemento in range(colunas):
            if elemento==numero:
                contador=contador+1
        indice=indice+1
    return contador