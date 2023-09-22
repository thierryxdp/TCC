def pontos_por_time(lista1,lista2):
    """calcula, dado duas listas de entrada contendo o nome dos times, e os seus respectivos gols nos jogos de ida(lista1) e nos jogos de volta(lista2),
    e retorna um dicionario com o numero de pontos de cada time, sendo que uma vitoria valhe 3 pontos, um empate valhe 1 ponto e uma derrota valhe 0 pontos
    lista, lista -> dicionario"""
    [[timeA,timeB],[gol_ida_timeA,gol_ida_timeB]]=lista1
    [[timeA,timeB],[gol_volta_timeA,gol_volta_timeB]]=lista2
    dicionario={}
    if gol_ida_timeA>gol_ida_timeB:
        dicionario[timeA]=3,dicionario[timeB]=0 
    elif gol_ida_timeA<gol_ida_timeB:
        dicionario[timeB]=3,dicionario[timeA]=0
    elif gol_ida_timeA==gol_ida_timeB:
        dicionario[timeA]=1,dicionario[timeB]=1
    elif gol_volta_timeA>gol_volta_timeB:
        dicionario[timeA]+=3
    elif gol_volta_timeA<gol_volta_timeB:
        dicionario[timeB]+=3
    elif gol_volta_timeA==gol_volta_timeB:
        dicionario[timeA]+=1,dicionario[timeB]+=1
        return dicionario