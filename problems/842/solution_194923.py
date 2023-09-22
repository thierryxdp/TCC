#Start your python function here
def pontos_por_time(Lrods):
    '''
        recebe uma lista com a informacao do resultado de jogos de ida e volta
        entre dois times e retorna os pontos acumulados
        entrada: lista
        saida: dicionario
    '''
    Lrod1=Lrods[0]
    Lrod2=Lrods[1]
    result1=Lrod1[2]
    result2=Lrod2[2]
    time1=Lrod1[0]
    time2=Lrod1[1]
    pontosT1=0
    pontosT2=0
    if result1[0]>result1[1]:
        pontosT1=3
    if result1[0]<result1[1]:
        pontosT2=3
    if result1[0]==result1[1]:
        pontosT1=1
        pontosT2=1
    if result2[0]>result2[1]:
        pontosT2=pontosT2+3
    if result2[0]<result2[1]:
        pontosT1=pontosT1+3
    if result2[0]==result2[1]:
        pontosT1=pontosT1+1
        pontosT2=pontosT2+1
    tabela={time1:pontosT1,time2:pontosT2}
    return tabela