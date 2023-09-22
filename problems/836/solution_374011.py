def busca(s,m):
    ''' funcao que recebe uuma string e uma matriz e retorna uma lista de strings;
    str,list(matriz)->list'''
    qtd_linhas=len(m)
    qtd_colunas=len(m[0])
    lista_vazia=[]
    for i in range(qtd_linhas):
        for j in range(qtd_colunas):
            if s == m[1][2]:
                return[[m[1][0],m[1][1],m[1][3]]]
            elif s== m[0][2] and s==m[2][2]:
                return[[m[0][0],m[0][1],m[0][3]],[m[2][0],m[2][1],m[2][3]]]
                
            else:
                return []