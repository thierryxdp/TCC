def pontos_por_time(saldo_das_partidas):
    """Dado o saldo de gols de duas partidas de um torneio entre Cormengo e Flaminthians, retorna 
    a tabela da soma dos resultados (vitória=3 pontos, empate= 1 pontos) dos times:
    list[['Cormengo','Flaminthians',[gols cor,gols fla]],['Flaminthians,'Cormengo',[gols fla,gols cor]]]
    -->dicionario{'Cormengo':pontuação,'Flaminthíans':pontuação}"""
    partida1=saldo_das_partidas[0]
    partida2=saldo_das_partidas[1]
    cor=[partida1[2][0],partida2[2][1]]
    fla=[partida1[2][1],partida2[2][0]]
    if cor[0]>fla[0] and cor[1]>fla[1]:
        return {'cormego':6,'flaminthians':2}
    elif cor[0]>fla[0] and cor[1]==fla[1]:
        return {'cormego':4,'flaminthians':1}
    elif cor[0]==fla[0] and cor[1]==fla[1]:
        return {'cormego':2,'flaminthians':2}
    elif cor[0]<fla[0] and cor[1]==fla[1]:
        return {'cormego':1,'flaminthians':4}
    elif cor[0]<fla[0] and cor[1]<fla[1]:
        return {'cormego':2,'flaminthians':6}
    else:
        return ""