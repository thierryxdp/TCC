def pontos_por_time(jogos):
    """essa função calcula e retorna o número de pontos acumulado por 2 times em 1 fase
dado o número de gols em 2 jogos de futebol entre esses times. Os pontos de um time na
fase são calculados da seguinte forma: em cada jogo, os times recebem 3 pontos
por vitória e 1 ponto por empate. não são atribuídos pontos para derrotas.
O total de pontos de uma fase  ́e a soma de pontos dos 2 jogos da fase. O parâmetro
de entrada da função é uma lista (jogos) com 2 elementos, onde cada um desses
elementos  ́e também uma lista. A lista completa tem informações do número de
gols em 2 jogos de futebol entre os dois times (jogo da ida e jogo da volta), no seguinte
formato: [[’Cormengo’, ’Flaminthians’, [1, 0]], [’Flaminthians’, ’Cormengo’, [2, 2]]].
list->dict"""
    time1=jogos[0][0]
    time2=jogos[0][1]
    pontos={str(time1): 0, str(time2): 0}
    if jogos[0][2][0] > jogos[0][2][1]:
        pontos[str(time1)] += 3
    if jogos[0][2][0] < jogos[0][2][1]:
        pontos[str(time2)]+= 3
    if jogos[0][2][0] == jogos[0][2][1]:
        pontos[str(time1)] += 1
        pontos[str(time2)] += 1
    if jogos[1][2][0] < jogos[1][2][1]:
        pontos[str(time1)] += 3
    if jogos[1][2][0] > jogos[1][2][1]:
        pontos[str(time2)] += 3
    if jogos[1][2][0] == jogos[1][2][1]:
        pontos[str(time1)] += 1
        pontos[str(time2)] += 1
    return pontos