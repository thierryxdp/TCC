def pontos_por_time(jogo_ida,jogo_volta):
    resultado=pontos_por_time
    resultado_ida=resultado[0][1]
    resultado_volta=resultado[1][1]
    if resultado_ida[0]>resultado_ida[1]:
        pontuacao_Time1=3
        pontuacao_Time2=0
        if resultado_ida[0]<resultado_ida[1]:
            pontuacao_Time1=0
            pontuacao_Time2=3
            if resultado_ida[0]==resultado_ida[1]:
                pontuacao_Time1=1
                pontuacao_Time2=1
                if resultado_volta[0]>resultado[1]:
                    pontuacao_Time2=pontuacao_Time2+3
                    if resultado_volta[0]<resultado_volta[1]:
                        pontuacao_Time1=pontuacao_Time1+3
                        if resultado_volta[0]==resultado_volta[1]:
                            pontuacao_Time1=pontuacao_Time1+1
                            pontuacao_Time2=pontuacao_Time2+1
                            return {resultado[0][0]:pontuacao_Time1,resultado[1][0]:pontuacao_Time2}