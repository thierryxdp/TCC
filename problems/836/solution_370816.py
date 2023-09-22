def busca(setor,matriz):
    '''busca os funcionários de um setor específico
    str,list(list) -> list'''
    achados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if setor in matriz[i][j]:
                achados.append(matriz[i]) 
    if len(achados) == 1:
        achados[0].remove(setor)
    if len(achados) == 2:
        achados[0].remove(setor)
        achados[1].remove(setor)
    return achados