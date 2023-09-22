def conta_numero(M, n):
    contador = 0
    for linhas in M:
        for colunas in linhas:
            if colunas == n:
               	contador += 1
    return contador