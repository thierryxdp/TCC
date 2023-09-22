def media_matriz(matriz):
    quantidade = 0
    soma = 0
    
    for m in matriz:
        for n in m:
            soma += n
            quantidade += 1
            
    media = round((soma / quantidade), 2)

    return media