'''Programa recebe matriz com 6 linhas, cada linha correspondendo a um piloto em uma bateria de kart,
com 10 voltas, e em cada linha, cada número inteiro representa o tempo de volta. O programa então retorna
uma tupla contendo o piloto que fez a melhor volta, o tempo da melhor volta e qual foi a melhor volta.
list -> tuple'''
def melhor_volta(matriz):
    numeros = []
    contador = 0
    volta = 0
    for A in matriz:
        for B in A:
        	numeros = numeros + [B]
    list.sort(numeros)
    melhortempovolta = numeros[0]
	while melhortempovolta not in matriz[contador]:
        volta = volta + 1
        contador = contador + 1
    volta = volta + 1
    qualvolta = list.index(matriz[volta - 1], melhortempovolta) + 1
    return (volta, melhortempovolta, qualvolta)