def busca(matriz,setor):
    '''funcao busca os funcionários do setor indicado. list,str->list'''
    c=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==setor:
                c.append(matriz[i])
    for k in range(len(c)):
        c[k].pop(2)
    return c