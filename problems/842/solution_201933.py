def pt(ls):
    d={name1(ls[0]):0, name1(ls[1]):0}
    p1=pontos(ls[0])
    contab(d,p1)
    p2=pontos(ls[1])
    contab(d,p2)
    return d