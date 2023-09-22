def pontos_por_time(resultados_da_fase):
    """funcao que retorna um dicionario contendo os pontos conquistados, sendo a chave de acesso a string do nome do clube;
    list ->dict"""
    placar_ida=resultados_da_fase[0][2]
    placar_volta=resultados_da_fase[1][2]
    Time1=resultados_da_fase[0][0]
    Time2=resultados_da_fase[0][1]
    pontuacao_Time1=[]
    pontuacao_Time2=[]

    if placar_ida[0]>placar_ida[1]:
        pontuacao_Time1=3
        pontuacao_Time2=0
        if placar_ida[0]<placar_ida[1]:
            pontuacao_Time1=0
            pontuacao_Time2=3
            if placar_ida[0]==placar_ida[1]:
                pontuacao_Time1=1
                pontuacao_Time2=1
                if placar_volta[0]>placar_volta[1]:
                    pontuacao_Time2=pontuacao_Time2+3
                    if placar_volta[0]<placar_volta[1]:
                        pontuacao_Time1=pontuacao_Time1+3
                        if placar_volta[0]==placar_volta[1]:
                            pontuacao_Time1=pontuacao_Time1+1
                            pontuacao_Time2=pontuacao_Time2+1
                            return {Time1:pontuacao_Time1,Time2:pontuacao_Time2}