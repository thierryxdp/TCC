def busca(setor,matriz):
    """Função que recebe com entrada uma matriz e o nome de um setor, a
    função retorna os dados de todos os funcionários daquele setor.
    str,list(list) -> list(list)
    """
    lista =[]
    for i in range(len(matriz)):
        if setor in matriz[i]:
            lista.append(matriz[i])
    for j in range(len(lista)):
        del lista[j][2]
    return lista