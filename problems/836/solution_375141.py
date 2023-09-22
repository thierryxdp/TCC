def busca(area,matriz):
    '''busca as informacoes de todos os funcionarios de uma area
    str,list -> list'''
    nlin=len(matriz)
    ncol=len(matriz[0])
    info=[]
    for i in range(nlin):
        if matriz[i][2]==area:
            list.append(info,matriz[i])
    for k in range(len(info)):
        list.pop(info[k],2)
    if info==[]:
        return info