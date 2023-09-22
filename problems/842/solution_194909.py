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
    pontosF=0
    pontosC=0
    if result1[0]>result1[1]:
        pontosC=3
    if result1[0]<result1[1]:
        pontosF=3
    if result1[0]==result1[1]:
        pontosF=1
        pontosC=1
    if result2[0]>result2[1]:
        pontosF=pontosF+3
    if result2[0]<result2[1]:
        pontosC=pontosC+3
    if result2[0]==result2[1]:
        pontosF=pontosF+1
        pontosC=pontosC+1
    tabela={'Cormengo':pontosC,'Flaminthians':pontosF}
    return tabela