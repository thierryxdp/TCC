def busca(setor, matriz):
    """Essa função, dado um nome de um setor de uma empresa e uma matriz com os dados dos funcionários armazenados,
	 retorna os dados de todos os funcionários daquele setor
	list -> list"""
    
    dados = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if setor in matriz[i]:
                matriz[i].remove(setor)
                dados.append(matriz[i])
                
    return dados