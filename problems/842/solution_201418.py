#Start your python function here
def pontos_por_time (L1,L2):
    L3=L1[2]
    L4=L2[2]
    times={L1[0],L1[1]}
    if L3[0]>L3[1]:
        if L4[1]>L4[0]:
            times['L1[0]'] = 6
            times['L1[1]'] = 0
            return times
        else:
            times['L1[0]'] = 3
            times['L1[1]'] = 3
            return times
    else:
        if L4[1]>L4[0]:
            times['L1[0]'] = 3
            times['L1[1]'] = 3
            return times
        else:
            times['L1[0]'] = 0
            times['L1[1]'] = 6
            return times