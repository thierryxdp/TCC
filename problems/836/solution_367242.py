def busca(setor,matriz):
    """Funcao que recebe uma matriz e faça uma busca por setor, essa
    funcao retorna os dados de todos os funcionarios daquele setor.
    Entrada: string, list
    Saída: list
    """
    lista = []
    elemento = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor: