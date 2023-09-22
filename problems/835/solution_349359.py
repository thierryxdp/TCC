def melhor_volta(voltas):
    """Dado uma lista de voltas, retorna o corredor com a volta mais rapida, o tempo da volta e qual foi a volta. list>tuple"""
	resultado=(0,120,0)
    for i in range(6):
        for j in range(10):
            if voltas[i][j]<resultado[1]:
                resultado= (i+1,voltas[i][j],j+1)
    return resultado