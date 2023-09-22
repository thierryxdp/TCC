def pontos_por_time(timesEGols):
    '''Função que retorna uma chave com os times e suas pontuações, dado uma lista timeEGols com duas listas com os times e os números de gols; list[list[str,str,list[int,int]],list[str,str,list[int,int]]]'''
    jogoDeIda=timesEGols[0]
    jogoDeVolta=timesEGols[1]
    placar1=jogoDeIda[2]
    placar2=jogoDeVolta[2]
    if placar1[0]>placar1[1] and placar2[1]>placar2[0]:
        return {jogoDeIda[0]:6,jogoDeIda[1]:0}
    elif placar1[1]>placar1[0] and placar2[0]placar2[1]:
        return {jogoDeIda[0]:0,jogoDeIda[1]:6}
    elif (placar1[0]>placar1[1] and placar2[0]>placar2[1])or (placar1[0]<placar1[1] and placar2[0]<placar2[1]):
        return {jogoDeIda[0]:3,jogoDeIda[1]:3}
    elif (placar1[1]==placar1[0] and placar2[1]>placar2[0]) or (placar1[0]>placar1[1] and placar2[1]==placar2[0]):
        return {jogoDeIda[0]:4,jogoDeIda[1]:1}
    elif (placar1[0]==placar1[1] and placar2[0]>placar2[1]) or (placar2[0]==placar2[1] and placar1[1]>placar1[0]):
        return {jogoDeIda[0]:1,jogoDeIda[1]:4}
    else:
        return {jogoDeIda[0]:2,jogoDeIda[1]:2}