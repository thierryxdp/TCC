def  busca(setor,matriz):
    '''
    Funçao que recebe as informaçoes dos funcionarios e um nome de um setor
    e retorna as informaçoes de todos os funcionarios desse setor
    str, list -> list
    '''
    resultado=[]
    for i in range(len(matriz)):
    	if matriz[i][2] == setor:                
            list.append(resultado,[matriz[i][0],matriz[i][1],matriz[i][3]])
	return resultado