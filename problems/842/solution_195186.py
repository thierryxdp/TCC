#Start your python function here
def pontos_por_time(lista):
    """Função que recebe uma lista composta por outras duas listas 
    que informam a respeito de dois jogos entre dois times; 
    cada lista contem o nome dos times e o placar do jogo,
    respectivamente. O retorno é um dicionário com o time e 
    a sua respectiva pontuação.
    list -> dict"""
    #[['time1','time2', [1, 0]], ['time2', 'time1', [2, 2]]]
    #                   0   1                       0   1
    #   0       1       2           0       1           2
    #           0                           1
    
    time1 = lista[0][0] = lista[1][1]
    time2 = lista[0][1] = lista[1][0]
    
    pontostime1 = 0
    pontostime2 = 0
    
    placar1_time1 = lista[0][2][0]
    placar1_time2 = lista[0][2][1]
    
    placar2_time1 = lista[1][2][1]
    placar2_time2 = lista[1][2][0]

    #primeira partida
    if placar1_time1>placar1_time2:
        pontostime1 = pontostime1+3
        
    if placar1_time1<placar1_time2:       
        pontostime2 = pontostime2+3
        
    if placar1_time1==placar1_time2:
        pontostime1=pontostime1+1
        pontostime2=pontostime2+1
        
    #segunda partida
    if placar2_time1>placar2_time2:
        pontostime1=pontostime1+3

    if placar2_time1<placar2_time2:      
        pontostime2=pontostime2+3
        
    if placar2_time1==placar2_time2:
        pontostime1=pontostime1+1
        pontostime2=pontostime2+1
        
    quadro_de_pontos = {time1: pontostime1, time2: pontostime2}
    return quadro_de_pontos

# casos de teste
# pontos_por_time([['Quebragalho','MandaChuva',[1,3]],['MandaChuva','Quebragalho',[2,1]]]) == {'Quebragalho': 0, 'MandaChuva': 6}
# pontos_por_time([['Flamengo','Vasco',[1,3]],['Vasco','Flamengo',[2,3]]]) == {'Flamengo': 3, 'Vasco': 3}
# pontos_por_time([['Cormengo','Flaminthians',[1,0]],['Flaminthians','Cormengo',[1,1]]]) == {'Cormengo': 4, 'Flaminthians': 1}