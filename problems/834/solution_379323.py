def media_matriz(matriz):
    """
    Dada uma matriz de inteiros nao vazia, retorna a media
    de todos os numeros da matriz com duas casas decimais de precisao;
    list->float
    """
    media_final = {}
    
    for i in matriz:
        num = matriz[i]
        media = 0
        total = 0
        for j in num:
            media += j
            total +=1
        media = media/total
        media_final[i] = media
    return media_final