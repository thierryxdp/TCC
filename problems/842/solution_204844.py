def pontos_por_time(ida, volta):
    if ida[2][0] > ida[2][1] and volta[2][1] > volta[2][0]:
        pontuacao = {'Cormengo':6, 'Flaminthias':0}
        return pontuacao
    elif ida[2][0] < ida[2][1] and volta[2][1] < volta[2][0]:
        pontuacao = {'Cormengo':0, 'Flaminthias':6}
        return pontuacao
    elif ida[2][0] > ida[2][1] and volta[2][1] < volta[2][0]:
        pontuacao = {'Cormengo':3, 'Flaminthias':3}
        return pontuacao
    elif ida[2][0] == ida[2][1] and volta[2][1] == volta[2][0]:
        pontuacao = {'Cormengo':1, 'Flaminthias':1}
        return pontuacao
    elif ida[2][0] == ida[2][1] and volta[2][1] > volta[2][0]:
        pontuacao = {'Cormengo':4, 'Flaminthias':1}
        return pontuacao
    elif ida[2][0] == ida[2][1] and volta[2][1] < volta[2][0]:
        pontuacao = {'Cormengo':1, 'Flaminthias':4}
        return pontuacao
    elif ida[2][0] > ida[2][1] and volta[2][1] == volta[2][0]:
        pontuacao = {'Cormengo':4, 'Flaminthias':1}
        return pontuacao
    elif ida[2][0] < ida[2][1] and volta[2][1] == volta[2][0]:
        pontuacao = {'Cormengo':1, 'Flaminthias':4}
        return pontuacao