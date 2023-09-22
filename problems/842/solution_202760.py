def pontos_por_time(x):
    e=x[0]
    v=x[1]
    ge=e[2]
    gv=v[2]
    if ge[0]>ge[1]:
        p1e=3
        p2e=0
    elif ge[0]<ge[1]:
        p1e=0
        p2e=3
    else:
        p1e=1
        p2e=1
    if gv[0]>gv[1]:
        p1v=3
        p2v=0
    elif gv[0]<gv[1]:
        p1v=0
        p2v=3
    else:
        p1v=1
        p2v=1
    pf1=p1e+p2v
    pf2=p2e+p1v
    
    pontuacao={e[0]:pf1, e[1]: pf2}
    return pontuacao