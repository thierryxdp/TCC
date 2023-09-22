#Questão 4
def melhor_volta(resultados):
    """Função que recebe uma matriz 6x10 com os resultados das
    voltas e retorna uma tupla com o melhor resultado;
    list -> tupla"""
    melhorResultado = ()
    melhorVolta = resultados[0][0]
    for i in range(len(resultados)):
        for j in range(len(resultados[0])):
            if resultados[i][j] < melhorVolta:
                melhorVolta = resultados[i][j]
                melhorResultado = (i, melhorVolta, j)
    return melhorResultado