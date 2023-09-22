def busca(chave,m):
    """Retorna os dados de todos os funcionários do setor dado
    str,list->list"""
    r = []
    for i in range(len(m)):
        if chave in m[i]:
            k = [m[i][0],m[i][1],m[i][3]]
            r.append(k)
    return r