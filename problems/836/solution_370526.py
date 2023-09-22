def busca (setor: str, matriz: list) -> list:
    """Função que dada uma matriz (onde todas as entradas são strings) com dados de funcionários de uma empresa, onde a primeira coluna são os nomes, a segunda os números, a terceira os setores e a quarta os números de telefone, faz uma busca nessa matriz por setor e retorna todos os funcionários e respectivos dados, daquele setor."""
	dados = []
	achados = []
    for i in range(len(matriz)):
        if setor in matriz[i][2]:
            list.extend(dados, matriz[i][0:2]) 
            list.extend(dados, matriz[i][3:4])
			list.append(achados,dados)
    return achados