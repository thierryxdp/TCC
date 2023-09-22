def pontos_por_time(L):
    """recebe uma lista de 2 elementos,onde cada elemento tambem e uma
    lista. retorna um dicionario cujos mapeamento sao:nome de um time->numero
    de pontos. list->dicionario"""
    
    jogoIda=L[0]
    placarIda=jogoIda[2]
    time1=jogoIda[0]
    time2=jogoIda[1]
    JogoVolta=L[1]
    placarVolta=jogoVolta[2]
    
    if placarIda[0]==placarIda[1]:
       return 'teste'