def busca(setor,matriz):
    """Dado o nome de um setor de uma empresa e uma matriz contendo em cada
    linha o nome da pessoa, registro, setor e telefone, a função retorna
    os dados de todos os funcionários daquele setor;
    str,list(list) -> list(list)"""

    matriz_dados1 = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            del matriz[i][2]
            list.append(matriz_dados1,matriz[i])
    return matriz_dados1