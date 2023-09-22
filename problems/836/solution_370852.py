def busca(setor, matriz):
    """Função que ao procurar os funcionarios de determinado setor dentro de uma matriz.
    Parametros: str, lista->lista"""
    lista_funcionarios = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(lista_funcionarios, del(matriz[i][2]))
    return lista_funcionarios