def busca(setor, matriz):
    """Retorna os dados de todos os funcionarios de um setor, dados: uma
    matriz e um nome de setor(deve ser dado entre aspas)."""
    
    dados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if setor in matriz[i]:
                matriz[i].remove(setor)
                dados.append(matriz[i])
	return dados