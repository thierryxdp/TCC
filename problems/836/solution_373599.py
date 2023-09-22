def busca(setor,matriz):
    pessoa = []
    for i in range(0,3):
        if matriz[i][2] == setor:
            pessoa += [matriz[i][0],matriz[i][1],matriz[i][3]]
            
    return pessoa