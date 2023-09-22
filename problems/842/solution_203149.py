#a função diz quantos pontos tem no final da fase de cada time,dada uma lista contendo as seguintes informações   [['Cormengo','Flaminthians', [gols do Cormengo, gols do Flaminthians]], ['Flaminthians', 'Flaminthians'[gols do Flaminthians , gols do Cormengo]]]
def pontos_por_time(list):
    p1 = 0
    p2 = 0 
    
    Cormengo = list[0][0]
    Flaminthians = list[0][1]
    
    if list[0][2][0]>list[0][2][1]:
        p1 = p1+3
    if list[0][2][0]<list[0][2][1]:
        p2 = p2+3
    if list[0][2][0]==list[0][2][1]:
        p1 = p1+1
        p2 = p2+1
    if list[1][2][0]<list[1][2][1]:
        p1 = p1+3
    if list[1][2][0]>list[1][2][1]:
        p2 = p2+3
    if list[1][2][0]==list[1][2][1]:
        p1 = p1+1
        p2 = p2+1
    return {Cormengo:p1 , Flaminthians:p2}

Conversar em #chat-secreto