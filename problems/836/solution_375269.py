def busca(setor, matriz):
    '''Retorna os dados de todos os funcionários do setor indicado,
    corforme a matriz inserida;
    str, list -> list'''
    funcionarios=[]
    for i in matriz:
        if i[2]==setor:
            dados=i
            dados.remove(setor)
            funcionarios.append(dados)
	return funcionarios