def busca(setor, matriz):
    """Funcao retorna uma lista com todos os funcionarios que trabalham no
    setor dado: setor a partir de uma matriz dada: matriz """

    funcionarios = []
    
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if setor.lower() == matriz[linha][coluna].lower():
                funcionarios.append(matriz[linha])

    return funcionarios