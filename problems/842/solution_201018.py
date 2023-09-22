def pontos_por_time(tabela_completa):
    """

    Função que retorna um dicionário com o nome do time e o total de pontos
    que ele obteve após os jogos d eida e volta, devnedo-se inserir com entrada:
    tabela_completa -> lista de 2 elementos, cada elemento é uma sub lista separada,
    tabela_1oturno = 1o turno, formato (nome dos times, resultado placar_ida)
    tabela_2oturno = 2o turno, formato (nome dos times, resultado placar_volta)

    [[str,str,[int,int],[str,str,[int,int]] -> dict{str:int,str:int}

    """

    tabela_1oturno = tabela_completa[0]
    tabela_2oturno = tabela_completa[1]
    placar_ida = tabela_1oturno[2]
    placar_volta = tabela_2oturno[2]
    if str(tabela_1oturno[0]) == str(tabela_2oturno[0]):
        if placar_ida[0] > placar_ida[1] and placar_volta[0] > placar_volta[1]:
            return {tabela_1oturno[0] : 6, tabela_1oturno[1] : 0}
        elif placar_ida[0] > placar_ida[1] and placar_volta[0] < placar_volta[1]:
            return {tabela_1oturno[0] : 3, tabela_1oturno[1] : 3}
        elif placar_ida[0] < placar_ida[1] and placar_volta[0] < placar_volta[1]:
            return {tabela_1oturno[0] : 0, tabela_1oturno[1] : 6}
        elif placar_ida[0] == placar_ida[1] and placar_volta[0] == placar_volta[1]:
            return {tabela_1oturno[0] : 2, tabela_1oturno[1] : 2}
        elif placar_ida[0] > placar_ida[1] and placar_volta[0] == placar_volta[1]:
            return {tabela_1oturno[0] : 4, tabela_1oturno[1] : 1}
        elif placar_ida[0] == placar_ida[1] and placar_volta[0] > placar_volta[1]:
            return {tabela_1oturno[0] : 4, tabela_1oturno[1] : 1}
        elif placar_ida[0] == placar_ida[1] and placar_volta[0] < placar_volta[1]:
            return {tabela_1oturno[0] : 1, tabela_1oturno[1] : 4}
        elif placar_ida[0] < placar_ida[1] and placar_volta[0] > placar_volta[1]:
            return {tabela_1oturno[0] : 3, tabela_1oturno[1] : 3}
        elif placar_ida[0] < placar_ida[1] and placar_volta[0] == placar_volta[1]:
            return {tabela_1oturno[0] : 1, tabela_1oturno[1] : 4}
    elif str(tabela_1oturno[0]) != str(tabela_2oturno[0]):
        if placar_ida[0] > placar_ida[1] and placar_volta[0] > placar_volta[1]:
            return {tabela_1oturno[0] : 3, tabela_1oturno[1] : 3}
        elif placar_ida[0] > placar_ida[1] and placar_volta[0] < placar_volta[1]:
            return {tabela_1oturno[0] : 6, tabela_1oturno[1] : 0}
        elif placar_ida[0] < placar_ida[1] and placar_volta[0] < placar_volta[1]:
            return {tabela_1oturno[0] : 3, tabela_1oturno[1] : 3}
        elif placar_ida[0] == placar_ida[1] and placar_volta[0] == placar_volta[1]:
            return {tabela_1oturno[0] : 2, tabela_1oturno[1] : 2}
        elif placar_ida[0] > placar_ida[1] and placar_volta[0] == placar_volta[1]:
            return {tabela_1oturno[0] : 4, tabela_1oturno[1] : 1}
        elif placar_ida[0] == placar_ida[1] and placar_volta[0] > placar_volta[1]:
            return {tabela_1oturno[0] : 1, tabela_1oturno[1] : 4}
        elif placar_ida[0] == placar_ida[1] and placar_volta[0] < placar_volta[1]:
            return {tabela_1oturno[0] : 4, tabela_1oturno[1] : 1}
        elif placar_ida[0] < placar_ida[1] and placar_volta[0] > placar_volta[1]:
            return {tabela_1oturno[1] : 6, tabela_1oturno[0] : 0}
        elif placar_ida[0] < placar_ida[1] and placar_volta[0] == placar_volta[1]:
            return {tabela_1oturno[0] : 1, tabela_1oturno[1] : 4}