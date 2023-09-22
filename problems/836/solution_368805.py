def busca(setor,matriz):
    '''funcao busca os funcionários do setor indicado. list,str->list'''
    c=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==setor:
                c.append(matriz[i])
    return c