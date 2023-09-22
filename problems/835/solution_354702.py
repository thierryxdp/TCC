def melhor_volta (matriz):
    'função que recebe matriz 6x10, contendo 10 tempos de 6 corredores de kart'
    'e retorna o corredor com o melhor tempo e em que volta'
    return (min(matriz),(list.index(matriz,min(matriz))+1))