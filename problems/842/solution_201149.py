def pontos_por_time(ls):
    """Funcao que recebera lista que possui
dois elementos, que sao outras listas, e retornara
dicionarios com o nome dos times e o numero
total de pontos de cada um na fase
assinatura: list --> dict
testes:
pontos_por_time([['Cormengo', "Flaminthians", [2, 0]], ['Flaminthians', "Cormengo", [2, 3]]]) == {'Cormengo': 6, 'Flaminthians': 0}
pontos_por_time([['Cormengo', "Flaminthians", [1, 1]], ['Flaminthians', "Cormengo", [1, 2]]]) == {'Cormengo': 4, 'Flaminthians': 1}
pontos_por_time([['Cormengo', "Flaminthians", [4, 5]], ['Flaminthians', "Cormengo", [2, 2]]]) == {'Cormengo': 1, 'Flaminthians': 4}"""

    ida = ls[0]
    vol = ls[1]
    ret = {ida[0] : 0, ida[1] : 0}

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

def contabilidade(d, t1, t2, gt1, gt2) :
    if gt1 > gt2:
        d[t1] = d[t1] + 3
    if gt2 > gt1:
        d[t2] += 3
    if gt1 == gt2:
        d[t1] += 1
        d[t2] += 1
    return d#Start your python function here