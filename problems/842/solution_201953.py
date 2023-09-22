def pontos_por_time(fase):
    """A função contabiliza os pontos dos times.
    assinatura: lista -> dic
    Casos de teste:
    ([['Flamínthian','Cormengo',[1,0]],[['Flamínthian','Cormengo',[2,2]]) == {'Flamínthians': 1, 'Cormengo': 4}
    ([['Flamínthian','Cormengo',[0,1]],[['Flamínthian','Cormengo',[4,5]]) == {'Flamínthians': 6, 'Cormengo': 0}
    """
    d = {fase[0][0]: 0, fase[0][1]: 0}
    ida = pontos(fase[0])
    contab(d,ida)
    volta = pontos(fase[1])
    contab(d,volta)
    return d

def pontos(fase):
    time_1 = fase[0]
    time_2 = fase[1]
    gols_time_1 = fase[2][0]
    gols_time_2 = fase[2][1]
    if gols_time_1 < gols_time_2:
        return (time_1, 0, time_2, 3)
    if gols_time_1 > gols_time_2:
        return (time_1, 3, time_2, 0)
    return (time_1, 1, time_2, 1)

d = {'cor':3,'fla':0}

def contab(d,t):
    time_1 = t[0]
    time_2 = t[2]
    d[time_1] = d[time_1] + t[1]
    d[time_2] = d[time_2] + t[3]