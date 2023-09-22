def pontos_por_time (x):
    '''
        recebe uma lista que tem duas informações, nas quais cada informação
        são outras listas contendo o número de gols dos dois jogos, um de ida
        e um de volta e retorna um dicionário com o nome do time e seus pontos. 
    '''
    n1 = gols_cormengo_jogo1
    n2 = gols_flaminthians_jogo1
    n3 = gols_cormengo_jogo2
    n4 = gols_flaminthians_jogo2
    a = pontos_cormengo_jogo1
    b = pontos_cormengo_jogo1
    a2 = pontos_cormengo_jogo2
    b2 = pontos_cormengo_jogo2
    if (n1>n2):
        return a=3 and b=0
    if (n2>n1):
        return a=0 and b=3
    if (n1=n2):
        return a=1 and b=1
    if (n3>n4):
        return a2=3 and b2=0
    if (n4>n3):
        return a2=0 and b2=3
    if (n4=n3):
        return a=1 and b=1
    return {'Cormengo':a+a2, 'Flaminthians':b+b2}