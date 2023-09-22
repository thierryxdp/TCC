def conta_numero(numero,matriz):
    'Dado um número e uma matriz, retorna a quantidad de vezes que o número aparece na matriz. Entradas: int, list[list]. Saída: int.'
    if matriz==[]:
        return 0
    linhas=len(matriz)
    colunas=len(matriz[0])
    qtd=0
    for l in range(linhas):
        for c in range(colunas):
            if matriz[l][c]==numero:
                qtd=qtd+1
    return qtd