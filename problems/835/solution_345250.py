def melhor_volta(matriz):
    """Esta é a função que dada uma matriz 6 X 10 que represente os 10 tempos de volta de cada corredor, retorna uma tupla contendo de quem foi a melhor volta, qual o tempo e em que volta; list -> tuple"""
    
    resultado = (0,float('inf'),0)

    for c in range(0,6):
        #c = corredores

       for v in range(0,10):
           #v = voltas

         if matriz[c][v] < resultado[1]:

               resultado = (c+1,matriz[c][v],v+1)

    return resultado