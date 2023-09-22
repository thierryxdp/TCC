def busca(chave,m):
    """Retorna os dados de todos os funcionários do setor dado
    str,list->list"""
    r = []
    for i in range(len(m)):
        if chave in m[i]:
            r.append(m[i][0])
            r.append(m[i][1])
            r.append(m[i][3])
    return r