def melhor_volta(m):
    tupla = ()
    qtd_linhas=len(m)
    qtd_colunas=len(m[0])
    for i in range(6):
        for j in range(10):
            if i and j  in m:
                return list.index(list(map(sum, m)) ,530),m[4][4],list.index(m[5],9)