#Start your python function here
def pontos_por_time(aaa):
    time1=0
    time2=0
    if aaa[0][2][0]>aaa[0][2][1]:
        time1=time1+3
    if aaa[0][2][0]<aaa[0][2][1]:
        time2=time2+3
    if aaa[0][2][0]==aaa[0][2][1]:
        time1=time1+1
        time2=time2+1
    if aaa[1][2][0]>aaa[1][2][1]:
        time1=time1+3
    if aaa[1][2][0]<aaa[1][2][1]:
        time2=time2+3
    if aaa[1][2][0]==aaa[1][2][1]:
        time1=time1+1
        time2=time2+1
    nome1=aaa[0][0]
    nome2=aaa[0][1]
    batata={nome1: time1, nome2: time2}
    return batata