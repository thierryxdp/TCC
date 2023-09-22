def pontos_por_time (x):
    '''
        Essa recebe uma lista que tem duas informações, nas quais cada informação
        são outras listas contendo o número de gols dos dois jogos, um de ida
        e um de volta e retorna um dicionário com o nome do time e seus pontos
    '''
    n1=pontos_time1=0
    n2=pontos_time2=0
    g1=gols_time1_jogo1=x[0[2[0]]]
    g2=gols_time2_jogo1=x[0[2[1]]]
    if (g1>g2):
        n1=n1+3
    if (g2>g1):
        n2=n2+3
    else:
        n1=n1+1
        n2=n2+1
    g11=gols_time1_jogo2
    g22=gols_time2_jogo2
    if (g11>g22):
        n1=n1+3
    if (g22>g11):
        n2=n2+3 
    else:
        n1=n1+1
        n2=n2+1
    return {x[0][0]: n1, x[0][1]:n2}