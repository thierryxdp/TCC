def busca(setor,matriz):
	'''Função que dado um setor e uma matriz em que cada linha tem quatro entradas,
	sendo elas nome, registro, setor e telefone de um funcionário, retorna os dados
	de todos os funcionários daquele setor.
	Entrada: string, lista de listas
	Saída: lista de listas''' 
    if matriz==[]:
        return 0
    else:
        linhas=len(matriz)
        colunas=len(matriz[0])
        ocorr=[]
        for i in range(linhas):
            if matriz[i][2] == setor:
                ocorrencia = []
                for j in range(colunas):
                    if matriz[i][j] != setor:
                        ocorrencia += [matriz[i][j]]
                ocorr += [ocorrencia]
        return ocorr