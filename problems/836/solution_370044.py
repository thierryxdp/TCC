def busca(setor, matriz_funcionarios):
    """
    Função que recebe uma string contendo um setor da empresa e uma matriz tal que cada linha da matriz tem as informações de um funcionário da empresa. A função retorna uma matriz cujas linhas contém as informações dos funcionários que pertencem ao setor recebido como parâmetro de entrada.
    Parâmetros:
    	setor: str
        matriz_funcionarios: list
    Saída:
    	list
    """
    funcionarios_setor = []
    for funcionario in matriz_funcionarios:
        if funcionario[2] == setor:
            funcionario_valido = funcionario[:]
            funcionario_valido.remove(setor)
            funcionarios_setor.append(funcionario_valido)
    return funcionarios_setor