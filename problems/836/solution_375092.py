def busca(setor,mat):
    ret = []
    for linhas in mat:
        if linhas[2]==setor:
            ret = list.append(ret,linhas)
    return ret