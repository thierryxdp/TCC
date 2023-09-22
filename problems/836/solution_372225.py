def busca(setor,matriz):
    a=[]
    for linhas in matriz:
        if linhas[2]==setor:
            a+=[[linhas[0],linhas[1],linhas[3]]]
    return a