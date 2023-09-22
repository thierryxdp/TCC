def busca(setor,matriz):
    """Função que recebe com entrada uma matriz e o nome de um setor, a
    função retorna os dados de todos os funcionários daquele setor.
    str,list(list) -> list(list)
    """
    lista =[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            lista += matriz[i]
    return lista