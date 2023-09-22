def busca(setor, matriz):
    """Funcao retorna uma lista com todos os funcionarios que trabalham no
    setor dado: setor a partir de uma matriz dada: matriz """

    funcionarios = []
    preenche = []
    
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if setor.lower() == matriz[linha][coluna].lower():
                preenche = []
                preenche.append(matriz[linha][0])
                preenche.append(matriz[linha][1])
                preenche.append(matriz[linha][3])
                funcionarios.append(preenche)

    return funcionarios