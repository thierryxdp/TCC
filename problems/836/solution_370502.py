def busca (setor: str, matriz: list) -> list:
    """Função que dada uma matriz (onde todas as entradas são strings) com dados de funcionários de uma empresa, onde a primeira coluna são os nomes, a segunda os números, a terceira os setores e a quarta os números de telefone, faz uma busca nessa matriz por setor e retorna todos os funcionários e respectivos dados, daquele setor."""
    dados = []
    for i in range(len(matriz[0])):
        achados = []
        if i == setor:
            list.append(achados, matriz[0][0:2])
            list.append(achados, matriz[0][3:4])
        	list.append(dados, achados)
    return dados