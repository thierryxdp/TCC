def media_matriz(matriz):
    soma = 0.0
    tamanho = 0.0

   
    for linha in matriz:
        
        for elemento in linha:
            
            soma += elemento
            
            tamanho += 1.0

    # Imprime a média com 2 casas decimais
    print("%0.2f" % (soma/tamanho))

    # Retorna a media
    return soma/tamanho