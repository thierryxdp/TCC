def pontos_por_time (x):
    '''
        Essa recebe uma lista que tem duas informações, nas quais cada informação
        são outras listas contendo o número de gols dos dois jogos, um de ida
        e um de volta e retorna um dicionário com o nome do time e seus pontos
        g representa os gols de cada time
        list-dict
    '''
    n1=pontos_time1=0
    n2=pontos_time2=0
    g1=x[0][2][0]
    g2=x[0][2][1]
    if (g1>g2):
        n1=n1+3
    if (g2>g1):
        n2=n2+3
    else:
        n1=n1+1
        n2=n2+1
    g3=x[1][2][0]
    g4=x[1][2][1]
    if (g3>g4):
        n1=n1+3
    if (g4>g3):
        n2=n2+3 
    else:
        n1=n1+1
        n2=n2+1
    return {x[0][0]: n1, x[0][1]:n2}