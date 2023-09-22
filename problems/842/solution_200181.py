def pontos_por_times(lista):
    
    pontos_Cormengo=0
    pontos_Flaminthians=0
    
    if lista[0][2][0]>lista[0][2][1]:
        pontos_Cormengo=pontos_Cormengo+3
    if lista[0][2][0]==lista[0][2][1]:
        pontos_Cormengo=pontos_Cormengo+1
        pontos_Flaminthians=pontos_Flaminthians+1
    if lista[0][2][0]<lista[0][2][1]:
        pontos_Flaminthians=pontos_Flaminthians+3
        
    elif lista[1][2][0]<lista[1][2][1]:
        pontos_Cormengo=pontos_Cormengo+3
    if lista[1][2][0]==lista[1][2][1]:
        pontos_Cormengo=pontos_Cormengo+1
        pontos_Flaminthians=pontos_Flaminthians+1
    if lista[1][2][0]>lista[1][2][1]:
        pontos_Flaminthians=pontos_Flaminthians+3
        
    tabela= {'Cormengo':pontos_Cormengo, 'Flamínthians':ponto_Flamínthians}
    return tabela