def melhor_volta(m):
    tupla = (0,flaot('a'),0)
    qtd_linhas=len(m)
    qtd_colunas=len(m[0])
    for i in range(6):
        for j in range(10):
            if m[i][j] < tupla[1]:
                tupla = (i+1,m[i][j],j+1)

    return tupla