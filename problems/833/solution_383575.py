def conta_numero(numero:int, matriz:list) ->int:
    '''Recebe um número inteiro e uma matriz e retorna quantas vezes aquele 
    numero aparece na matriz.'''
    contador = 0
    for linha in matriz:
        for elemento in linha:
            if numero == elemento:
                contador +=1 
    return contador