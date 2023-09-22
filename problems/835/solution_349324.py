def melhor_volta(matriz):
    '''
    Retorna a melhor volta da prova
        Parametros:
            matriz: list
        Saida: tuple
    '''
    tupla = ()

    for i in range(1,7):
        tupla += (min(a[i]),tupla.index(a[i]))

    return tupla