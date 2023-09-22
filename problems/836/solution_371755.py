def busca(setor,matriz):
    """Função que recbe um setor e uma matriz e retorna os dados das pessoas
        desse setor.
        str, lis -> list """
    resultado = []
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if setor.lower() == matriz[lin][col].lower():
                dados = matriz[lin].copy()
                dados.pop(dados.index(dados[col]))
                resultado.append(dados)

    return resultado