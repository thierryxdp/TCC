def busca(setor,matriz):
    '''
    	Função que recebe um setor do tipo string e uma matriz com informações do funcionario, e retorna
        todos os funcionarios em uma matriz com suas informações.
        str, list -> list
    '''
    result = []
    result2 = []
    for i in range(0,len(matriz)):
    	for j in range(0,len(matriz[0])):
        	if matriz[i][j] == setor:
                result.append(matriz[i])
    for i in range(0,len(result)):
    	for j in range(0,len(result[0])):
            if result[i][j] != setor:
                result2.append(result[i][j])
    return result2