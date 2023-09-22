def pontos_por_time(ls):
    """Funçao que recebe uma lista de 2 elementos, sendo outras listas, e retorna dicionários
com o nome do time e o número total de pontos na fase
assinatura: list --› dict
testes:
pontos_por_time([['Cormengo',"Flaminthians", [1,0]], ['Flaminthians',"Cormengo",[2,2]]]) == {'Cormengo': 4, 'Flaminthians': 1}
pontos_por_time([['Cormengo',"Flaminthians", [1,1]], ['Flaminthians',"Cormengo",[0,0]]]) == {'Cormengo': 2, 'Flaminthians': 2}
pontos_por_time([['Cormengo','Flaminthians', [10,0]], ['Flaminthians',"Cormengo",[1,0]]]) == {'Cormengo': 3, 'Flaminthians': 3}
"""
    ida = ls[0] # lista da ida
    vol = ls[1] # lista da volta
    ret = {ida[0]: 0, ida[1]: 0}

    t1 = ida[0] # nome do time 1
    t2 = ida[1] # nome do time 2
    gt1 = ida[2][0] # gols do time 1
    gt2 = ida[2][1] # gols do time 2
    contabilidade(ret, t1, t2, gt1, gt2)

    t1 = vol[0] # nome do time 1
    t2 = vol[1] # nome do time 2
    gt1 = vol[2][0] # gols do time 1
    gt2 = vol[2][1] # gols do time 2
    contabilidade(ret, t1, t2, gt1, gt2)
    return ret

def contabilidade(d, t1, t2, gt1, gt2) :
    if gt1 > gt2: # situação em que t1 ganhou
        d[t1] = d[t1] + 3
    if gt2 > gt1: # situação em que t2 ganhou
        d[t2] += 3
    if gt1 == gt2: # situação em que t1 e t2 empataram
        d[t1] += 1
        d[t2] += 1
    return d