def busca(setor, matriz):
	dados = []

	for linha in matriz:
       	if linha[2] == setor:
            del linha[2]:
            	dados = dados + linha
                
                return dados