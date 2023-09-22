def conta_numero(n,m):
    """função que recebe um número inteiro e uma matriz, e analisa
    quantas vezes esse número aparece nessa matriz. E que deve retornar
    a quantidade de vezes que esse número aparece;
    int,matriz->int"""
    linhas = range(len(m))
    colunas = range(len(m[0]))
    qtd_num = 0
    for i in linhas:
        for j in colunas:
            if m[i][j]==n:
                qtd_num = qtd_num+1
    return qtd_num