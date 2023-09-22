def pontos_por_time (result):
    """recebe uma lista com as informações dos jogos e retorna um dicionario com os nomes dos times e suas pontuações
    list->dict"""
    if result[0][2][0]>result[0][2][1]:
        x=3 
    elif result[0][2][0]<result[0][2][1]:
        y=3
    elif result[1][2][0]>result[1][2][1]:
        a=3
    elif result[1][2][0]<result[1][2][1]:
        b=3
    elif result[0][2][0]==result[0][2][1]:
        x=1
        y=1
    elif result[1][2][0]==result[1][2][1]:
        b=1
        a=1
    mapeamento={'Cormengo':(x+a),'Flamínthians':(y+b)}
    return mapeamento