def busca(informacao,matriz):
    ''' '''
    matriz_nova=[]
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if informacao == matriz[linha][coluna]:
                matriz_nova.append(matriz[linha])
    			matriz_nova.pop(3)
    return matriz_nova