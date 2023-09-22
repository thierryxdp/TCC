def pontos_por_time(l):
    '''Função que retorna os pontos de um time em um campeonato
    	list(list(str,str,list(int,int)),(list(str,str,list(int,int))) -> dict'''
    x=l[0]
    y=l[1]
    z=x[2]
    w=y[2]
    if z[0]>z[1]:
        p11=3
    if z[0]==z[1]:
        p11=1
    if w[1]>w[0]:
        p21=3
    if w[1]==w[0]:
        p21=1
    if z[1]>z[0]:
        p12=3
    if z[0]==z[1]:
        p12=1
    if w[0]>w[1]:
        p22=3
    if w[0]==w[1]:
        p22=1
    return {x[0]:p11+p21,x[1]:p21+p22}