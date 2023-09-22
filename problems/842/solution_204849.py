def pontos_por_time(ida):
    if ida[2][0] > ida[2][1] and volta[2][1] > volta[2][0]:
        pontuacao = {ida[0]:6, ida[1]:0}
        return pontuacao
    elif ida[2][0] < ida[2][1] and volta[2][1] < volta[2][0]:
        pontuacao = {ida[0]:0, ida[1]:6}
        return pontuacao
    elif ida[2][0] > ida[2][1] and volta[2][1] < volta[2][0]:
        pontuacao = {ida[0]:3, ida[1]:3}
        return pontuacao
    elif ida[2][0] == ida[2][1] and volta[2][1] == volta[2][0]:
        pontuacao = {ida[0]:1, ida[1]:1}
        return pontuacao
    elif ida[2][0] == ida[2][1] and volta[2][1] > volta[2][0]:
        pontuacao = {ida[0]:4, ida[1]:1}
        return pontuacao
    elif ida[2][0] == ida[2][1] and volta[2][1] < volta[2][0]:
        pontuacao = {ida[0]:1, ida[1]:4}
        return pontuacao
    elif ida[2][0] > ida[2][1] and volta[2][1] == volta[2][0]:
        pontuacao = {ida[0]:4, ida[1]:1}
        return pontuacao
    elif ida[2][0] < ida[2][1] and volta[2][1] == volta[2][0]:
        pontuacao = {ida[0]:1, ida[1]:4}
        return pontuacao