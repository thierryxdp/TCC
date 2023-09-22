def busca(setor,mat):
    ret = []
    i=0
    for linhas in mat:
        if linhas[2]==setor:
            list.append(ret,linhas)
            list.pop(ret[i],2)
            i+=1
    return ret