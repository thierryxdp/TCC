def pontos_por_time(lista):
    '''função em que dada uma lista de dois elementos que são listas. A lista completa tem informações do número de gols em dois
    jogos de futebol entre o timeA e o timeB em jogos de ida e volta, no seguinte
    formato: [[timeA,timeB>,[GolTimeA,GolTimeB]],
    [timeA,timeB,[GolTimeB,GolTimeA]]]. A saída consiste no nome dos times e as suas pontuaçoes list->dict'''
    tabela1={lista[0][0]:6,lista[1][0]:0}
    
    tabela2={lista[0][0]:3,lista[1][0]:3}
    
    tabela3={lista[0][0]:0,lista[1][0]:6}
    
    tabela4={lista[0][0]:4,lista[1][0]:1}
    
    tabela5={lista[0][0]:1,lista[1][0]:4}
    
    tabela6={lista[0][0]:2,lista[1][0]:2}
    
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
        return tabela1
    
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
        return tabela2
    
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
        return tabela2
    
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
        return tabela3
    
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
        return tabela4
    
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
        return tabela4
    
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
        return tabela5
    
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
        return tabela5
    
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
        return tabela6