def busca(s,m):
    qtd_linhas=len(m)
    qtd_colunas=len(m[0])
    lista_vazia=[]
    for i in range(qtd_linhas):
        for j in range(qtd_colunas):
            if s == m[1][2]:
                lista_vazia=[[m[1][0],m[1][1],m[1][3]]]
            elif s== m[0][2] and s==m[2][2]:
                lista_vazia=[m[0][0],m[0][1],m[0][3]],[m[2][0],m[2][1],m[2][3]]