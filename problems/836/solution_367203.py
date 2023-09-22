def busca(setor, matriz):
    """Essa função, dado um nome de um setor de uma empresa e uma matriz com os dados dos funcionários armazenados,
	 retorna os dados de todos os funcionários daquele setor
	list -> list"""
    
    i = 0
    dados = []
    for m in matriz:
        i += 1
        for n in m:
            if setor in n:
                list.append(dados, [m[i][0], m[i][1]])
        
    return dados