def busca(s,m):
    ''' retorna os dados de todos os funcionários dao setor s, dada uma matriz m e o nome do setor s;
    str, mat -> mat '''
    x = []
    for i in range(len(m)):
        if s == m[i][2]:
            list.remove(m[i],s)
            list.append(x,m[i])
    return x