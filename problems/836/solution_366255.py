def busca(s,m):
    """ a funçaõ recebe um setor e retorna os dados dos funcionários daquele setor;
    str,list->list"""
    funcionarios = []
    for i in range(len(m)):
        if s in m[i][2]:
            del m[i][2]
            list.append(funcionarios,m[i])
    return funcionarios