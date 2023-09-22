def busca(setor,matriz):
    """	
    	retorna as informações dos funcionários de dado setor
    	str,list -> list
    """
    funcionarios=[]
    for i in range(len(matriz)):
        if setor == matriz[i][2]:
            funcionarios.append([matriz[i][0],matriz[i][1],matriz[i][3])
    return funcionarios