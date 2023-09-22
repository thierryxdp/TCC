def melhor_volta(matriz):
    '''Coloque uma lista em forma de matriz com os tempos de cada um dos corredores e o resultado será o corredor que teve a melhor volta, o tempo da melhor volta e qual foi a volta
       list->tuple'''
    tupla = (0,float('inf'),0)

    for i in range(6):

        for j in range(10):

            if matriz[i][j] < tupla[1]:

                tupla = (i+1,matriz[i][j],j+1) #de quem, tempo, qual volta

    return tupla