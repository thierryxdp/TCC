def media_matriz(matriz):
    soma = 0
    tamanho = 0

    # Para cada linha da matriz
    for linha in matriz:
        # Para cada elemento da linha
        '''
        for elemento in linha:
            # Soma o elemento à variável soma
            soma += elemento
            # Adiciona 1 ao tamanho da matriz
            tamanho += 1
        '''
        soma+=sum(linha)
        tamanho+=len(linha)
        print(len(linha))
        print(linha)

    # Imprime a média com 2 casas decimais
    #print("%0.2f" % (soma/tamanho))
    #print(tamanho)

    # Retorna a media
    return round(soma/(tamanho+1),2)