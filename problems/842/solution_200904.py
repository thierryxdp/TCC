def pontos_por_time(l):
    """recebe uma lista de dois elementos, cada um sendo
também uma lista, e retorna um dicionário cujos mapeamentos
são: <nome do time> -> <número total de pontos na fase>
assinatura: list --> dict
testes:pontos_por_time([['F', 'C', [1,2]], ['C', 'F', [1,1]]]) == {'F' : 1, 'C' : 4}
pontos_por_time([['C', 'F', [2,1]], ['F', 'C', [1,1]]]) == {'C' : 4, 'F' : 1}
    """
    ida = l[0]
    volta = l[1]
    ret = {ida[0] : 0, ida[1] : 0}

    t1 = ida[0]
    t2 = ida[1]
    ret[t1] = 0
    ret[t2] = 0

    gols = ida[2]
    g1 = gols[0]
    g2 = gols[1]
    pontuacao(ret, t1, t2, g1, g2)

    t1 = volta[1]
    t2 = volta[0]

    gols = volta[2]
    g1 = gols[0]
    g2 = gols[1]
    pontuacao(ret, t1, t2, g1, g2)

    return ret

def pontuacao(d, t1, t2, g1, g2):
    if g1 > g2:
        d[t1] += 3

    if g1 == g2:
        d[t1] += 1
        d[t2] += 1
    if g1 < g2:
        d[t2] += 3