def pontos_por_time(lista):
    dicionario = {}
    timeA1 = lista[0][0]
    timeB1 = lista[0][1]
    timeA2 = lista[1][0]
    timeB2 = lista[1][1]
    
    gols1= lista [0][2]
    gols2=lista [1][2]
    if gols1[0] ==gols1[1]:
        dicionario[timeA1] =+1
        dicionario[timeB1] =+1
    if gols1 [0] > gols1 [1]:
        dicionario [timeA1] =+3
        dicionario [timeB1 =+0
	if gols1 [0] <gols1 [1]:
        dicionario [timeB1]=+3
        dicionario [timeA1] =+0

    if gols2[0] == gols2[1]:
        dicionario[timeA2]=+1
        dicionario[timeB2]=+1
    if gols2[0] > gols2[1]:
        dicionario[timeA2]=+3
        dicionario[timeB2]=+0
	if gols2[0] <gols2[1]:
        dicionario[timeB2]=+3
        dicionario[timeA2]=+0
        
    return dicionario