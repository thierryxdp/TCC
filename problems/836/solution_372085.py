def busca(setor,matriz):
    """	
    	retorna as informações dos funcionários de dado setor
    	str,list -> list
    """
    funcionarios=[]
    for i in range(len(matriz)):
        if setor == matriz[i][2]:
            funcionarios.append(matriz[i])
    return funcionarios