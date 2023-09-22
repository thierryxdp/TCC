def conta_numero(n, M):
    contador = 0
    for linhas in M:
        for colunas in linhas:
            if colunas == n:
               	contador += 1
    return contador