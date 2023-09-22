def busca(setor, matriz):
    """Essa função, dado um nome de um setor de uma empresa e uma matriz com os dados dos funcionários armazenados,
	 retorna os dados de todos os funcionários daquele setor
	list -> list"""
    
    dados = []
    
    
    for linha in matriz:
        for coluna in linha:
            if coluna[2] == setor:
                list.append(dados, coluna)
                
                
    return dados