def busca(setor: str, matriz: list)-> list:

    dados_setor = []

    for setor_buscado in range(len(matriz)):
        if str.lower(setor) in str.lower(matriz[setor_buscado][2]):
            contato= list.remove (setor_buscado, setor)
            list.append(dados_setor,Matriz(contato))

    return dados_setor