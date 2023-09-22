def busca(setor,matriz):
    '''Busca e retorna as matrizes que contém dado setor'''
    x=[]
    for i in range(len(matriz)):
        if setor==matriz[i][2]:
            x=x+[matriz[i][0],matriz[i][1],matriz[i][2]]
    return [x]