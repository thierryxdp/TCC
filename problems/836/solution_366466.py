def busca(setor,m):
    """funcao que dados uma matriz com as informacoes referentes aos
       funcionarios e o setor que se deseja pesquisar retorna os dados de
       todos os funcionarios daquele setor

       str, lista-> lista
    """

    nlinhas= len(m)
    ncolunas=4
    funcionarios=[]

    for i in range(nlinhas):
            if m[i][3] == setor:
                list.remove(m[i],m[1][2])
                list.append(funcionarios, (m[i])
                            return funcionarios