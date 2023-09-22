def busca(informacao,matriz):
    '''Função que pega a matriz de entrada e verifica se a informação de entrada está contida nela,
    deste modo, ela retorna uma matriz sem essa informação, apenas as informações da linha correspondente
    a da informação passa permanecem.
    list,list→list'''
    matriz_nova=[]
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])-1):
            if informacao == matriz[linha][coluna]:
                lista1=matriz[linha]
                lista1.remove(informacao)
                matriz_nova.append(lista1)
    return matriz_nova