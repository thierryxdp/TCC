def melhor_volta(matriz):
    '''retorna de quem foi a melhor volta, 
    com qual tempo e em que volta; entrada-> matriz 6x10;
    list(mat)-> tupla'''
    tupla= ()
    maior=100
    for linha in matriz:
        for elem in linha:
            if elem <= maior:
                maior = elem
    return maior