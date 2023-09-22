#Start your python function here
time1=lista[0][0]
    time2=lista[0][1]
    ptstime1=0
    ptstime2=0
    golstime1p1=lista[0][2][0]
    golstime1p2=lista[1][2][1]
    golstime2p1=lista[0][2][1]
    golstime2p2=lista[1][2][0]
    if golstime1p1>golstime2p1:
        ptstime1 = ptstime1+3
    if golstime2p1>golstime1p1:
        ptstime2 = ptstime2+3
    if golstime2p1==golstime1p1:
        ptstime1 = ptstime1+1
    if golstime1p1==golstime2p1:
        ptstime2 = ptstime2+1
    if golstime1p2>golstime2p2:
        ptstime1 = ptstime1+3
    if golstime2p2>golstime1p2:
        ptstime2 = ptstime2+3
    if golstime2p2==golstime1p2:
        ptstime1 = ptstime1+1
    if golstime1p2==golstime2p2:
        ptstime2 = ptstime2+1
    return {time1:ptstime1,time2:ptstime2}