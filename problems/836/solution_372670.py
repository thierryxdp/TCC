def busca (setor, matriz):
    '''função que recebe uma matriz contendo informações de 
       funcionarios de uma empresa. Dado um setor, retorna os
       dados de todos os funcionarios desse setor.
       : str, list -> list
    '''
    resultado = []
    nlin = len(matriz)
    ncol = len(matriz[0])
    
    for i in range(nlin):
        for j in range(ncol):
            if matriz[i][2] == setor:
                del(matriz[i],j)
            resultado += matriz[i]
    return resultado