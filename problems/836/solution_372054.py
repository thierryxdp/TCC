def busca(setor, matriz):
    """Função que ao inserir um setor de entrada, retorne os dados dos funcionários que trabalham nele"""
    """Parâmetros de entrada:list"""
    """Parâmetros de saída: str"""
	contador=0
    acumulador=[]
    while contador<len(matriz):
        if matriz[contador][2]==setor:
            acumulador+=[matriz[contador][0],matriz[contador][1],matriz[contador][3]]
    	contador+=1
    return [acumulador]