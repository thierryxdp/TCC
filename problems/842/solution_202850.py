def pontos_por_time(tabela):
    """
    Função recebe uma lista com strings dos nomes dos times e mais uma lista
    com o resultados dos jogos. Por fim, a função retorna um dicionário com
    a pontuação final da fase.
    lista --> dicionário
    """
    
    if tabela[0][0] == tabela[1][0] and tabela[0][1] == tabela[1][1]:
        time1 = tabela[0][0]
        time2 = tabela[0][1]
    else:
        return "Ordem alterada ou nomes de times distintos."

    pontuacaoTime1 = 0
    pontuacaoTime2 = 0

    if tabela[0][2][0] > tabela[0][2][1]:
        pontuacaoTime1 = pontuacaoTime1 + 3
    elif tabela[0][2][0] < tabela[0][2][1]:
        pontuacaoTime2 = pontuacaoTime2 + 3
    else:
        pontuacaoTime1 = pontuacaoTime1 + 1
        pontuacaoTime2 = pontuacaoTime2 + 1


    if tabela[1][2][0] > tabela[1][2][1]:
        pontuacaoTime1 = pontuacaoTime1 + 3
    elif tabela[1][2][0] < tabela[1][2][1]:
        pontuacaoTime2 = pontuacaoTime2 + 3
    else:
        pontuacaoTime1 = pontuacaoTime1 + 1
        pontuacaoTime2 = pontuacaoTime2 + 1

    tabelaFinal = {
        time1: pontuacaoTime1,
        time2: pontuacaoTime2
    }

    return tabelaFinal