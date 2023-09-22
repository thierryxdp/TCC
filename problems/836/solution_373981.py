def busca(s,m):
    qtd_linhas=len(m)
    qtd_colunas=len(m[0])
    lista_vazia=[]
    for i in range(qtd_linhas):
        for j in range(qtd_colunas):
            if s == m[1][2]:
                lista_vazia=m[1][0],m[1][1],m[1][3]