def busca(setor,matriz):
    """função que recebe uma matriz e faz uma busca por setor, retornando os dados dos funcionários;
    str,list -> list"""
    acumulador = [ ]
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            list.append(acumulador,matriz[i])
    for c in range(len(acumulador)):
        del acumulador[c][2]
    return acumulador