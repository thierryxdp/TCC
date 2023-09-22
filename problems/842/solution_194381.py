def pontos_por_time (L2):
    """Recebe uma lista dois elementos, ambos listas com o formato ''[time], [time, [gol para cada time]" duas vezes, uma para o jogo de ida e outra pro
    de volta. Então, a função calcula o total de pontos para cada time""".
    lista1 = L2[0]
    lista2 = L2[1]
    
    AGols1 = lista1[0]
    BGols1 = lista1[1]
    AGols2 = lista2[0]
    BGols2 = lista2[1]
    if AGols1>BGols1 or AGols2>BGols2:
        TeamA = 3
    elif AGols1<BGols1 or AGols2<BGols2:
    	TeamB = 3
   	elif AGols1 = BGols1 or AGols2 = BGols2:
    	TeamA = 1 and TeamB = 1
    return {<lista1[0]> + '->' + TeamA
            <lista2[0]> + '->' + TeamB}