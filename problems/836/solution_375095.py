def busca(setor,mat):
    ret = []
    for linhas in mat:
        if linhas[2]==setor:
            list.append(ret,linhas)
            list.pop(ret,2)
    return ret