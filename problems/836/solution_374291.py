def busca(setor,matriz):
    m = matriz
    s = 'setor'
    registro = 0
    for i in range(0,len(matriz)):
        if s in matriz[i]:
            del matriz[i][2]
            registro += [matriz[i]]
        return registro