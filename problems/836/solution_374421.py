def busca(informacao,matriz):
    ''' '''
    matriz_nova=[]
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])-1):
            if informacao == matriz[linha][coluna]:
                lista1=matriz[linha]
                lista1.remove(informacao)
                matriz_nova.append(lista1)
    return matriz_nova