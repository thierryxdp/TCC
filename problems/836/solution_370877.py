def busca(setor: str, matriz: list)-> list:
    """Função que dado o setor e uma matriz contendo os dados de funcionários de uma empresa,
    retorna uma lista com os dados de todos os funcionários do setor buscado."""

    dados_setor = []

    for setor_buscado in range(len(matriz)):
        if str.lower(setor) in str.lower(matriz[setor_buscado][2]):
            list.append(dados_setor,matriz[setor_buscado])
            dados_setor.remove(setor_buscado)

    return dados_setor