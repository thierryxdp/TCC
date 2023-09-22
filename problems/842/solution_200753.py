def pontos_por_time(ls):
    """Recebe uma lista de dois elementos (onde os elementos também são
listas) com informações sobre dois times e seus gols feitos em jogos de
ida e volta respectivamente. Retorna um dicionário com o nome do time e os pontos
na fase (contando que, vitória valem três pontos e empate um ponto).
assinatura: list --> dict
casos de testes:
pontos_por_time([['Cormengo', 'Flaminthians', [1, 0]], ['Flaminthians', 'Cormengo', [2, 2]]]) == {'Cormengo': 4, 'Flaminthians': 1}
pontos_por_time([['São Paulo', 'Flamengo', [3, 2]], ['Flamengo', 'São Paulo', [1, 1]]]) == {'São Paulo': 4, 'Flamengo': 1}
pontos_por_time([['Fluminense', 'Santos', [1, 1]], ['Fluminense', 'Santos', [1, 1]]]) == {'Fluminense': 2, 'Santos': 2}
pontos_por_time([['Palmeiras', 'Vasco', [4, 0]], ['Vasco', 'Palmeiras', [1, 3]]]) == {'Palmeiras': 6, 'Vasco': 0}
"""
    ida = ls[0] #Pacaembu, ['Cormengo', 'Flaminthians', [1, 0]]
    vol = ls[1] #Maracanã, ['Flaminthians, 'Cormengo', [2, 2]]
    ret = {ida[0]: 0, ida[1]: 0}

    t1 = ida[0]
    t2 = ida[1]
    gt1 = ida[2][0]
    gt2 = ida[2][1]
    contabilidade(ret, t1, t2, gt1, gt2)
    

    t1 = vol[0]
    t2 = vol[1]
    gt1 = vol[2][0]
    gt2 = vol[2][1]
    contabilidade(ret, t1, t2, gt1, gt2)
    return ret

def contabilidade(d, t1, t2, gt1, gt2):
    if gt1 < gt2:
        d[t2] += 3
    if gt2 < gt1:
        d[t1] += 3
    if gt2 == gt1:
        d[t2] += 1
        d[t1] += 1