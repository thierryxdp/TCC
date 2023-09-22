def pontos_por_time ([[ida],[volta]]):
    """recebe uma lista com as informações dos jogos e retorna um dicionario com os nomes dos times e suas pontuações
    list->dict"""
    if ida[2][0]>ida[2][1]:
        x=3
    elif ida[2][0]<ida[2][1]:
        y=3
    elif volta[2][0]>ida[2][1]:
        a=3
    elif volta[2][0]<ida[2][1]:
        b=3
    elif ida[2][0]==ida[2][1]:
        x=1
        y=1
    elif volta[2][0]==ida[2][1]:
        b=1
        a=1
    resultado1=x+a
    resultado2=y+b
    mapeamento={'Cormengo':resultado1,'Flamínthians':resultado2}
    return mapeamento