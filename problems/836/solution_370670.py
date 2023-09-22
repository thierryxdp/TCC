def busca(setor, matriz):
    """Dado o nome de um setor da empresa, retorna os dados de todos os funcionários daquele setor,
    onde os dados de todos os funcionários da empresa estão contidos em uma matriz
    input: setor -> string, matriz -> list
    output: funcionarios -> list
    """
    funcionarios = []
    for i in range(len(matriz)):
        if str.find((matriz[i][2]).lower(), setor.lower()) != -1:
            funcionarios = funcionarios + [matriz[i][:2] + matriz[i][3:]]
    return funcionarios