def busca(setor, matriz):
    """Essa função, dado um nome de um setor de uma empresa e uma matriz com os dados dos funcionários armazenados,
	 retorna os dados de todos os funcionários daquele setor
	list -> list"""
    
    dados = []
    i = 0
    
    for linha in matriz:
        for coluna in linha:
            i = i + 1
            if setor in coluna[i]:
                list.append(dados, coluna)
                
                
    return dados