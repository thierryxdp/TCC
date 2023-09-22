def pontos_por_time(lista):
    """A função recebe uma lista cujos elementos são duas
    listas, cada uma contendo strings com os nomes de 2 times
    e outra lista com o placar do jogo entre eles. O retorno
    da função é um dicionário cujas chaves são uma string com o 
    nome de cada time e os valores são ints correspondentes à
    pontuação total dos times."""
    pontos1 = 0
    pontos2 = 0
    if ((lista[0])[2])[0] > ((lista[0])[2])[1]:
        pontos1 += 3
    if ((lista[0])[2])[0] < ((lista[0])[2])[1]:
        pontos2 += 3
    if ((lista[0])[2])[0] == ((lista[0])[2])[1]:
        pontos1 += 1
        pontos2 += 1
        
    pontos3 = 0
    pontos4 = 0
    if ((lista[1])[2])[0] > ((lista[1])[2])[1]:
        pontos3 += 3
    if ((lista[1])[2])[0] < ((lista[1])[2])[1]:
        pontos4 += 3
    if ((lista[1])[2])[0] == ((lista[1])[2])[1]:
        pontos3 += 1
        pontos4 += 1
        
    time1 = (lista[0])[0]
    time2 = (lista[0])[1]
    if (lista[1])[0] == time1:
        pontos_time1 = pontos1+pontos3
        pontos_time2 = pontos2+pontos4
    if (lista[1])[0] == time2:
        pontos_time1 = pontos1+pontos4
        pontos_time2 = pontos2+pontos3
        
        return {time1:pontos_time1, time2:pontos_time2}