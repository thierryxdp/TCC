def media_matriz(matriz):
    """ Recebe uma matriz e retorna a media aritimetica;
    list[???][???] --> float"""
    
    # Conta a quantidade de numeros que tem na matriz
    contador_Num = 0
    
    soma_Num = 0

    for linha in matriz:
        for coluna in linha:
            contador_Num += 1
            soma_Num += coluna

    return round((soma_Num / contador_Num),2)