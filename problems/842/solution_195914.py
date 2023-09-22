def pontos_por_time(l):
    h=int(l[0][2][1])
    g=int(l[0][2][0])
    k=int(l[1][2][1])
    j=int(l[1][2][0])
    pontos_t1=[0]
    pontos_t2=[0]
    if g>h:
        pontos_t1[0] = pontos_t1[0]+3
    elif g==h:
        pontos_t1[0] = pontos_t1[0]+1
        pontos_t2[0] = pontos_t2[0]+1
    elif g<h:
        pontos_t2[0] = pontos_t2[0]+3
    if k>j:
        pontos_t1[0] = pontos_t1[0]+3
    elif k==j:
        pontos_t1[0] = pontos_t1[0]+1
        pontos_t2[0] = pontos_t2[0]+1
    elif k<j:
        pontos_t2[0] = pontos_t2[0]+3
    zz=pontos_t1[0]
    zx=pontos_t2[0]
    p={l[0][0]:zz,l[0][1]:zx}
    return p