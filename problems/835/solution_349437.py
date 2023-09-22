def melhor_volta(matriz):
    """funcao que dada uma matriz 6 x 10 retorna uma tupla informando de quem foi a melhor volta, qual tempo e em qual volta"""
    """list->tupla"""
    resultado = ()
    tempos = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.append(tempos, matriz[i][j])
    tempominimo = min(tempos)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == tempominimo:
      		    resultado = resultado + (i + 1,)
                resultado = resultado + (tempominimo,)
                resultado = resultado + (j + 1,)
    return resultado