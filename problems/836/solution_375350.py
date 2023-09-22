def busca(setor, matriz):
    """Recebe uma matriz de uma empresa com os dados
    e retorna os dados das pessoas do setor selecionado;
    list[???][???],str --> list[???][???]"""
    
    funcionario_Setor = []
    
    for funcionario in matriz:
        if funcionario[2] == setor:
            funcionario_Setor.append([funcionario[0],funcionario[1],funcionario[3]])

    return funcionario_Setor