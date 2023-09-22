def pontos_por_time(L1,L2):
    L1[2]=a
    L2[2]=b
    if a[0]>a[1]:
        cormengo_ida=3
    if a[0]<a[1]:
        flaminthians_ida=3
    if a[0]==a[1]:
        cormengo_ida=1
        flaminthians_ida=1
    if b[0]>b[1]:
        cormengo_volta=3
    if b[0]<b[1]:
        flaminthians_volta=3
    if b[0]==b[1]:
        flaminthians_volta=1
        flaminthians_volta=1
    return {'Vasínthians':cormengo_ida+cormengo_volta,\
            'Fluminantos':flaminthians_ida+flaminthians_ida}