def media_matriz(matriz):
    '''Função que retorna a média de todos os numeros
    da matriz com duas casas decimais.
    list -> float
    '''
    m = 0
    Sn = 0
    for numero in matriz:
        for num in numero:
            Sn += num
            m += 1
    media = Sn/m
    return round(media,2)