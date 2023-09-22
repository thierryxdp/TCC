def busca(setor,matriz):
    """A função recebe uma matriz como entrada. Cada linha
    da matriz tem quatro entradas, mencionando informações
    como nome, registro, setor e telefone - nesta ordem. O
    número de linhas depende da quantidade de funcionários.
    Todas as entradas estão seguindo o formato string. A
    função deve buscar pelo setor da empresa, e retornar
    os dados de todos os funcionários daquela área.
    Entrada: List(String)
    Saída: List"""
    
    todos=[]
    informacao=[]
    for i in range(len(matriz)):
        if setor in matriz[i][2]:
            matriz[i].remove(setor)
            informacao += matriz[i]
    return informacao