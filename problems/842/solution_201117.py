resultadoJogo = []
resultadoJogo = ['Flamengo', 'Fluminense', [1, 0]]
listaResultados = []
listaResultados.append(resultadoJogo)
resultadoJogo = ['Fluminense', 'Flamengo', [2, 2]]
listaResultados.append(resultadoJogo)

def pontos_por_time(listaResultados):
    
    pontos_flamengo = 0
    pontos_fluminense = 0

    if listaResultados[0][2][0] > listaResultados[0][2][1]:
        if listaResultados[0][0] == 'Flamengo':
            pontos_flamengo += 3
        else:
            pontos_fluminense += 3
    elif listaResultados[0][2][0] < listaResultados[0][2][1]:
        if listaResultados[0][0] == 'Flamengo':
            pontos_flamengo += 3
        else:
            pontos_fluminense += 3
    else:
        pontos_flamengo += 1
        pontos_fluminense += 1

    if listaResultados[1][2][0] > listaResultados[1][2][1]:
        if listaResultados[0][0] == 'Flamengo':
            pontos_flamengo += 3
        else:
            pontos_fluminense += 3
    elif listaResultados[0][2][0] < listaResultados[0][2][1]:
        if listaResultados[0][0] == 'Flamengo':
            pontos_flamengo += 3
        else:
            pontos_fluminense += 3
    else:
        pontos_flamengo += 1
        pontos_fluminense += 1
    dicionario = {'Flamengo': pontos_flamengo, 'Fluminense' : pontos_fluminense}
    return dicionario







# Faça uma função chamada pontos_por_time que receba uma lista de dois elementos, onde cada elemento é também uma lista. A lista completa tem informações do número de gols em
# dois jogos de futebol entre dois times (jogo da ida e jogo da volta), no seguinte formato: [['Flamengo', 'Fluminense', [1, 0]], ['Fluminense', 'Flamengo', [2, 2]]]. Nesta 
# lista de exemplo, no primeiro jogo entre Flamengo e Fluminense, o Flamengo fez 1 gol e o Fluminense não fez gol. Sua função deve retornar um dicionário cujos mapeamentos são:
# <nome do time> -> <numero total de pontos na fase>. Os pontos de um time na fase são calculados da seguinte forma: em cada jogo, os times recebem três pontos por vitória e um ponto por empate.
# Não são atribuídos pontos para derrotas. O total de pontos de uma fase é a soma de pontos dos dois jogos da fase. Na lista de exemplo, o total de pontos do Flamengo é 4 e do Fluminense é 1.