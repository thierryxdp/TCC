#Start your python function here
#
def pontos_por_time(placar1,placar2):
    if placar1[2][1]>placar1[2][2] and placar2[2][2]>placar2[2][1]:
        return {flaminthians=0,cormengo=6}
    elif placar1[2][1]<placar1[2][2] and placar2[2][2]<placar2[2][1]:
        return {flaminthians=6,cormengo=0}
    elif placar1[2][1]=placar1[2][2] and placar2[2][2]>placar2[2][1]:
        return {flaminthians=1,cormengo=4}
    elif placar1[2][1]>placar1[2][2] and placar2[2][2]=placar2[2][1]:
        return {flaminthians=1,cormengo=4}
    elif placar1[2][1]=placar1[2][2] and placar2[2][2]<placar2[2][1]:
        return {flaminthians=4,cormengo=1}
    elif placar1[2][1]>placar1[2][2] and placar2[2][2]=placar2[2][1]:
        return {flaminthians=4,cormengo=1}