def conta_numero(n,mat):
    """A função que conta quantas vezes um inteiro n aparece
    numa matriz.
     int, matriz/list --> int"""
    qtd=0
    for linhas in mat:
        for elementos in linhas:
            if elementos == n :
                qtd+=1
    return qtd