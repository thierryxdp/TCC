def media_matriz(matriz):
    #  lista de lista (matriz) --> float
    num_linhas = len(matriz)
    num_elementos=0
    soma=0
    for i in range(0,num_linhas):
        num_colunas=len(matriz[i])
        for j in range(0,num_colunas):
            num_elementos= num_elementos + 1
            soma = soma + matriz[i][j]
    media = soma/num_elementos
    saida={:.2f}.format(media)
    return saida