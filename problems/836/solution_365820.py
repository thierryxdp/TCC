def busca(setor, matriz):
    """Função que dada uma matriz com os dados de funcionários de uma empresa e retorna o dado dos funcionários de 
    determinado setor
    list(list), string -> list(list)"""
    funcionarios = []
    for i in range(len(matriz)):
        if setor in matriz[i][2]:
            list.append(funcionarios, matriz[i])
    return funcionarios