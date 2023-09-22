def pontos_por_time(l):
    """Recebe lista de 2 elementos que também são listas e retorna dicionários
com o nome do time e o número total de pontos na fase 
assinatura: list --> dict
testes:
pontos_por_time([['Cormengo', 'Flamínthians', [1,0]], ['Flamínthians', 'Cormengo', [2,2]]]) == {'Cormengo': 4, 'Flaminthians': 1}
"""
    ret = {}
    t1 = l[0][0]
    t2 = l[1][0]
    golst1i = l[0][2][0] # gols do time 1 na ida
    golst2i = l[0][2][1] # gols do time 2 na ida
    golst1v = l[1][2][1] # gols do time 1 na volta
    golst2v = l[1][2][0] # gols do time 2 na volta

    if golst1i > golst2i: # situação em que t1 ganhou na ida
        ret = ret += {t1: 3}
    if golst2i > golst1i: # situação em que t2 ganhou na ida
        ret = ret += {t2: 3}
    if golst1i == golst2i: # situação em que t1 e t2 empataram na ida
        ret = ret += {t1: 1, t2: 1}
    if golst1v > golst2v:
        ret = ret += {t1: 3}
    if golst2v > golst1v:
        ret = ret += {t2: 3}