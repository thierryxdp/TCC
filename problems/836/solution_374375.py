def busca(informacao,matriz):
    ''' '''
    matriz_nova=[]
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if informacao == matriz[linha][coluna]:
                matriz_nova.append(matriz[linha])
            elif informacao in matriz_nova:
                del.matriz_nova(informacao)
    return matriz_nova