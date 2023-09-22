def busca (setor: str, matriz: list) -> list:
    """Função que dada uma matriz (onde todas as entradas são strings) com dados de funcionários de uma empresa, onde a primeira coluna são os nomes, a segunda os números, a terceira os setores e a quarta os números de telefone, faz uma busca nessa matriz por setor e retorna todos os funcionários e respectivos dados, daquele setor."""
    dados = []
    for i in range (len(matriz)):
        linha = []
        for j in range (len(matriz[0])):
            if matriz[i][2] == setor:
                list.append(linha,matriz[i][j])
        list.append(dados, linha)
    	del dados[i][2:3]
        for i in range (len(dados)):
        	if dados[i][2] != setor:
            	del dados[i]
    return dados