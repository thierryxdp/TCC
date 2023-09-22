def busca(setor,mat):
    ret = []
    for linhas in mat:
        if linhas[2]==setor:
            list.append(ret,linhas)
            list.remove(ret,setor)
    return ret