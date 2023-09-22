def melhor_volta (matriz):
    'função que recebe matriz 6x10, contendo 10 tempos de 6 corredores de kart'
    'e retorna o corredor com o melhor tempo e em que volta. list->tupla'
    n=()
    for i in range (len (matriz)):
        for j in range (len (matriz)[i]):
            n=n+((min(matriz)[i]),)
    return n