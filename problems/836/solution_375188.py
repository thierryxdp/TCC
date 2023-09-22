def busca(setor, matriz):
	""" Dado uma matriz com os dados funcionários de e um setor, retorna os dados de todos os funcionario daquel setor.
    entrada matriz -> saida lista."""
    
    dados = []
   
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            dados = matriz[i]
            
    return dados