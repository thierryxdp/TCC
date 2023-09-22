def busca(setor,matriz):
    '''
    	Função que recebe um setor do tipo string e uma matriz com informações do funcionario, e retorna
        todos os funcionarios em uma matriz com suas informações.
        str, list -> list
    '''
    result = []
    for i in range(0,len(matriz)):
    	for j in range(0,len(matriz[0])):
        	if matriz[i][j] == setor:
                result.append(matriz[i])
                del(result[result.index(setor)])
    return result