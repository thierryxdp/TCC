def pontos_por_time (lista):
    """Recebe uma lista de dois elementos, cada um sendo uma lista em si. A lista
    completa tem o saldo de gols em dois jogos entre dois times tendo como saída um
    dicionário com o nome dos times e seus respectivos pontos.
    list -> dict"""
    tabela1={lista[0][0]:6,lista[1][0]:0}
    tabela2={lista[0][0]:3,lista[1][0]:3}
    tabela3={lista[0][0]:0,lista[1][0]:6}
    tabela4={lista[0][0]:4,lista[1][0]:1}
    tabela5={lista[0][0]:1,lista[1][0]:4}
    tabela6={lista[0][0]:2,lista[1][0]:2}
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
    #Time 1 ganha os 2 jogos.
        return tabela1
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
    #Time 1 ganha o primeiro, Time 2 o segundo.
        return tabela2
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
    #Time 1 ganha o segundo, Time 2 o primeiro.
        return tabela2
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
    #Time 2 ganha os 2 jogos.
        return tabela3
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
    #Time 1 ganha o primeiro e empata o segundo.
        return tabela4
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
    #Time 1 ganha o segundo e empata o primeiro.
        return tabela4
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
    #Time 2 ganha o primeiro e empata o segundo.
        return tabela5
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
    #Time 2 ganha o segundo e empata o primeiro.
        return tabela5
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
    #Empate nos dois jogos
        return tabela6