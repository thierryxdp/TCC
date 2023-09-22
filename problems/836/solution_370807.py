def busca(setor,matriz):
    '''busca os funcionários de um setor específico
    str,list(list) -> list'''
    achados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if setor in matriz[i][j]:
                achados.append(matriz[i])
    if setor in achados:
        achados.remove(setor,5)
    return achados