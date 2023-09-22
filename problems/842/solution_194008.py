def pontos_por_time(['time1', + 'time2', + [gol1,gol2]],['time1', + 'time2', + [gol3,gol4]]):
    ""","""
    if gol1>gol2:
        return gol1*3
    elif gol1<gol2:
        return gol2*3
    elif gol1=gol2:
        return gol1 or gol2
    if gol3>gol4:
        return gol3*3
    elif gol3<gol4:
        return gol4*3
    elif gol3=gol4:
        return gol3 or gol4
    return {'time1': gol1+gol3, 'time2': gol2+gol4}