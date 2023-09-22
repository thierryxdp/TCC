f pontos_por_time(ls):
    """Assinatura: list --> dict
Calcular a pontuação dos times
Testes:
{"Fla": 1, "Cor":4} == pontos_por_time([['Cor', 'Fla', [1,0]], ['Fla', 'Cor', [2,2]]])
{"A": 3, "B":3} == pontos_por_time([['A', 'B', [10,0]], ['B', 'A', [1,0]]])
{"B": 3, "A":3} == pontos_por_time([['A', 'B', [10,0]], ['B', 'A', [1,0]]])
"""

    ida = ls[0] #Pacaembu, ['Cor', 'Fla', [1,0]]
    vol = ls[1] #maracanã, ['Fla', 'Cor', [2,2]]
    ret = {ida[0]: 0, ida[1]: 0}
#ida
    t1 = ida[0]
    t2 = ida[1]
    gt1 = ida[2][0]
    gt2 = ida[2][1]
    contabilidade(ret, t1, t2, gt1, gt2)
    
#volta
    t1 = vol[0]
    t2 = vol[1]
    gt1 = vol[2][0]
    gt2 = vol[2][1]
    contabilidade(ret, t1, t2, gt1, gt2)
    return ret


def contabilidade (d, t1,t2, gt1, gt2):

    if gt1 < gt2:
        d[t2] += 3 # ret[t2] = ret[t2] + 3
    if gt2 < gt1:
        d[t1] += 3
    if gt2 == gt1:
        d[t2] += 1
        d[t1] += 1