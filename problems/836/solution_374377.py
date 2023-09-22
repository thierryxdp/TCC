def busca(informacao,matriz):
    ''' '''
    matriz_nova=[]
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if informacao == matriz[linha][coluna]:
                matriz_nova.append(matriz[linha])
    for linha in range(len(matriz_nova)):
        for coluna in range(len(matriz_nova[linha])):
            indice= matriz_nova.index(informacao)
            matriz_nova.pop(indice)
    return matriz_nova