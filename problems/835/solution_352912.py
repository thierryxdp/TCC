def melhor_volta(m):
    tupla = ()
    qtd_linhas=len(m)
    qtd_colunas=len(m[0])
    a=list(map(sum, m))
    for i in range(6):
        for j in range(10):
            if i and j in m:
                return list.index(list(map(sum, m)),541),m[3][6] ,list.index(m[4],34)