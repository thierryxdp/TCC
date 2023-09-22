#Start your python function here
def pontos_por_time (jogos):
    """ receba uma lista de dois elementos, onde cada elemento é também uma lista.
    A lista completa tem informações do número de gols em dois jogos de futebol entre dois times (jogo da ida e jogo da volta),
    no seguinte formato: [['Cormengo', 'Flamínthians', [1, 0]], ['Flamínthians', 'Cormengo', [2, 2]]].
    
    Nesta lista de exemplo, no primeiro jogo entre Cormengo e Flamínthians, o Cormengo fez 1 gol e o Flamínthians não fez gol. 
    a função retorna um dicionário cujos mapeamentos são: <nome do time> -> <numero total de pontos na fase>. 
    
    
    Os pontos de um time na fase são calculados da seguinte forma: em cada jogo, os times recebem três pontos por vitória e um ponto por empate. Não são atribuídos pontos para derrotas. O total de pontos de uma fase é a soma de pontos dos dois jogos da fase. 
    Na lista de exemplo, o total de pontos do Cormengo é 4 e do Flamínthians é 1."""
    
    time1=jogos[0][0]
    time2=jogos[0][1]
    placar1[0][2]
    placar2[1][2]
    
    gols_time1j1=placar1 [0]
    gols_time2j1=placar1 [1]
    gols_time1j2=placar2[1]
    gols_time2j2=placsr2 [0]
    
    if gols_time1j1> gols_time2j1:
        pontos_t1=3
    if gols_time1j1 <gols_time2j1:
        pontos_t2=3
    if gols_time1j1== gols_time2j1:
        pontos_t1=1
        pontos_t2=1
    if gols_time1j2> gols_time2j1:
        pontos_t1=pontos_t1+3
    if gols_time1j2 <gols_time2j2:
        pontos_t2=pontos_t2+3
    if gols_time1j2==gols_timej2:
        pontos_t1=pontos_t1+1
        pontos_t2=pontos_t2+1
    
    return {time1:pontos_t1, time2:pontos_t2}