def melhor_volta(matriz):
    '''dada uma matriz, a funçao retorna dados os tempo de cada volta qual
    piloto fez a melhor volta, qual o tempo da melhr volta e qual foi o 
    numero da volta que o piloto obteve a seguinte volta
    list--->tupl'''
    minimo = []
    for i in matriz:
        minimo = minimo + [min(i)]
    tempo1 = min(minimo)
    x = list.index(minimo, tempo1)
    melhorVolta = list.index(matriz[x], tempo1)
    return (x+1,tempo1,melhorVolta+1)