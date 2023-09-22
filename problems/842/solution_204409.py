def pontos_por_time(jogos):
    ida = jogos[0]
    volta = jogos[1]
    p1 = ida[2]
    p2 = volta[2]
    r1 = {ida[0]:p1[0],ida[1]:p1[1]}
    r2 = {volta[1]:p2[1],volta[0]:p2[0]}

    if r1[ida[0]]>r1[ida[1]]:
        Tabela = {ida[0]:3,ida[1]:0}
        if r2[volta[0]]>r2[volta[1]]:
            Tabela = {ida[0]:6,ida[1]:0}
            return Tabela
        elif r2[volta[0]]==r2[volta[1]]:
            Tabela = {ida[0]:4,ida[1]:1}
            return Tabela
        else:
            Tabela = {ida[0]:3,ida[1]:3}
            return Tabela

    if r1[ida[0]] == r1[ida[1]]:
        Tabela = {ida[0]:1,ida[1]:1}
        if r2[volta[0]]>r2[volta[1]]:
            Tabela = {ida[0]:4,ida[1]:1}
            return Tabela
        elif r2[volta[0]]==r2[volta[1]]:
            Tabela = {ida[0]:2,ida[1]:2}
            return Tabela
        else:
            Tabela = {ida[0]:1,ida[1]:4}
            return Tabela

    if r1[ida[0]]<r1[ida[1]]:
        Tabela = {ida[0]:0,ida[1]:3}
        if r2[volta[0]]>r2[volta[1]]:
            Tabela = {ida[0]:3,ida[1]:3}
            return Tabela
        elif r2[volta[0]]==r2[volta[1]]:
            Tabela = {ida[0]:1,ida[1]:4}
            return Tabela
        else:
            Tabela = {ida[0]:0,ida[1]:6}
            return Tabela