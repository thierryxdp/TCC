def pontos_por_time(a,b):
    a = ['time1', 'time2', [gol1,gol2]]
    b = ['time2', 'time1', [gol3,gol4]]
    if gol1>gol2:
        gol1*3
    if gol1<gol2:
        gol2*3
    if gol3>gol4:
        gol3*3
    if gol3<gol4:
        gol4*3
    return {'time1':gol1+gol3,'time2':gol2+gol4}