def busca(setor, matriz):
    """Função que faz uma busca por setor em uma matriz dada
    str,list-> list"""
    
    if setor not in matriz:
        return []
    for i in range(0, len(matriz)):
        teste = False
        for j in range(0, len(matriz)):
            if matriz[i][j] == setor:
                teste = True
        if teste == False:
            matriz.pop(matriz[i][j])     
    return matriz