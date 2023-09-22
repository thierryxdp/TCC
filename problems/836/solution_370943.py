def busca(setor, matriz):
    """Função que dada uma matriz retorna todos os dados de um funcionário exceto o nome do setor da empresa.
    str, list --> list"""
    listinha = []
    
    for lista in range(len(matriz)):
        if setor in matriz[lista][2]:
            list.append(listinha, [matriz[lista][0], matriz[lista][1], matriz[lista][3]])
            
    return listinha