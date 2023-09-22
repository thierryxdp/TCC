def busca(string: str, matriz: list)-> list:
    """Dada uma string, contendo o nome de um setor da empresa, e uma
    matriz, na qual cada linha possui quatro entradas: nome, registro,
    setor e telefone de um funcionário nesta ordem. A função retorna
    uma lista com os dados de todos os funcionários daquele setor dado.
    Caso não encontre nenhum registro, a função retorna uma lista vazia"""
    lista = list()
    numlinhas = len(matriz)
    numcolunas = len(matriz[0])
    for i in range(numlinhas):
        for j in range(numcolunas):
            if string in matriz[i][2]:
                lista.pop(2)
                list.append(lista, matriz[i][j])
    return lista