def busca(setor: str, matriz: list)-> list:

    dados_setor = []

    for setor_buscado in range(len(matriz)):
        if str.lower(setor) in str.lower(matriz[setor_buscado][2]):
            list.append(dados_setor,matriz[setor_buscado])
            list.remove(dados_setor[setor_buscado-1],setor)

    return dados_setor