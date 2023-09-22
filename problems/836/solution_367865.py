def busca(setor, matriz):
    '''funcao que dada uma matriz e o nome de um setor, retorna as informações de todos os funcionarios daquele setor
       string, matriz(strings) -> list(strings)'''
    resultado = []
    j = 0
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
        	del(matriz[i][2])
            list.append(resultado,matriz[i])
    return resultado