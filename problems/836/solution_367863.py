def busca(setor, matriz):
    '''funcao que dada uma matriz e o nome de um setor, retorna as informações de todos os funcionarios daquele setor
       string, matriz(strings) -> list(strings)'''
    resultado = [[]]
    j = 0
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
        	resultado[j] = [matriz[i][0], matriz[i][1], matriz[i][3]]
            j += 1
    return resultado