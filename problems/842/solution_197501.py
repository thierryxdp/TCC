def pontos_por_time(lista):
    j1=lista[0]
    j2=lista[1]
    a=j1[2][0]
    b=j1[2][1]
    c=j2[2][0]
    d=j2[2][1]
    pt1=''
    pt2=''
    if a>b:
        pt1=pt1+'3'
        pt2=pt2+'0'
    if a<b:
        pt1=pt1+'0'
        pt2=pt2+'3'
    if a==b:
        pt1=pt1+'1'
        pt2=pt2+'1'
    if c<d:
        pt1=pt1+'3'
        pt2=pt2+'0'
    if c>d:
        pt1=pt1+'0'
        pt2=pt2+'3'
    if c==d:
        pt1=pt1+'1'
        pt2=pt2+'1'
    pt1=int(pt1[0])+int(pt1[1])
    pt2=int(pt2[0])+int(pt2[1])
    dic={j1[0]:pt1,j2[0]:pt2}
    return dic