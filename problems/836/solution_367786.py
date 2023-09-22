def busca(setor,matriz):
    """
    Dada uma matriz na qual cada linha contem os dados de um funcionario
    de uma empresa (nome,numero,setor,telefone) e um setor a ser buscado
    nela, retorna-se os dados dos funcionarios que sejam desse setor.
    Entradas:
    	setor -> string
        matriz -> list(lists)
    Retorna: list ou list(lists)
    """
    funcionarios = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            funcionarios = funcionarios + [matriz[i][0] + matriz[i][1] + matriz[i][3]]
    return funcionarios