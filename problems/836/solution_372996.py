def busca(setor,matriz):
    '''Dado um setor e uma matriz, retorna os dados dos funcionarios do setor
    buscado; string, list[list[str]] -> list[str]'''
    i=0
    result = []
    for linha in matriz:
        if matriz[i][2] == setor:
            result.append(matriz[i])
            result.remove(matriz[i][2])
        i+=1
    return result