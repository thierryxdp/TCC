def busca (setor, matriz):
    '''função que recebe uma matriz contendo informações de 
       funcionarios de uma empresa. Dado um setor, retorna os
       dados de todos os funcionarios desse setor.
       : str, list -> list
    '''
    resultado = []
    nlin = len(matriz)
    ncol = len