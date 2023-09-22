def pontos_por_time(L):
    '''Recebe uma lista com duas listas dentro, uma com informações (nome dos times e número de gols por time) de um primeiro jogo de futebol entre dois times, e a outra, com essas mesmas informações sobre o segundo jogo, e retorna um dicionário cuja chave é o nome do time e cujo valor é o total de pontos:
    list -> dict'''
   
    time1 = L[0][0]
    time2 = L[0][1]        
    p1=0
    p2=0
       
    if L[0][2][0] > L[0][2][1]:
        p1=p1+3
    elif L[0][2][0] < L[0][2][1]:
        p2=p2+3
    else:
        p1=p1+1
        p2=p2+1
    if L[1][2][0] > L[1][2][1]:
        p2=p2+3
    elif L[1][2][0] < L[1][2][1]:
        p1=p1+3
    else:
        p1=p1+1
        p2=p2+1  
   
    return { time1 : p1, time2 : p2 }