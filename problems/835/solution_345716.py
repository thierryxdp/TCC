def melhor_volta(lista):
    '''
    Avalia uma lista com valores de voltas de kart
    e identifica a melhor volta, retornando o número
    do corredor, o tempo e o número da volta;
    list -> tuple(int, float)
    '''
    
    melhorCorredor = 0
    melhorVolta = min(lista[0])
    numeroVolta = lista[0].index(min(lista[0]))
    
    contador = 0
    for linha in lista:
        if min(linha) < melhorVolta:
            melhorCorredor = contador
            melhorVolta = min(linha)
            numeroVolta = linha.index(min(linha))
        contador += 1
    return (melhorCorredor + 1, melhorVolta, numeroVolta + 1)