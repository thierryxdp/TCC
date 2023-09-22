def conta_numero(numero, matriz):
    '''funçao dado um numero e uma matriz retorna quantas vezes esse numero aparece dentro da matriz
    int, list -> int'''
    contador = 0
    for indice in matriz:
        if type(indice) == list:
            for elemento in indice:
                if elemento == numero:
                    contador += 1
        if indice == numero:
            contador += 1
    return contador