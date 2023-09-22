def busca(setor, matriz):
    """Essa função, dado um nome de um setor de uma empresa e uma matriz com os dados dos funcionários armazenados,
	 retorna os dados de todos os funcionários daquele setor
	list -> list"""
    
    i = 0
    dados = []
    for m in matriz:
        for n in m:
            if setor in n:
                list.append(dados, [n[0], n[1]])
        i += 1
    return dados