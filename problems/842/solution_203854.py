def pontos_por_time(l):
    '''Retorna um dicionário com a pontuação total de cada time na fase
    list -> dict'''
    pontos={}
    a=bool(l[0][2][0]>l[0][2][1])
    b=bool(l[0][2][0]==l[0][2][1])
    c=bool(l[1][2][1]>l[1][2][0])
    d=bool(l[1][2][1]==l[1][2][0])
    
    cor=(a+c)*3+(b+d)
    
    if (b+d)==2:
        fla=cor
    if (b+d)==1:
        fla=5-(cor)
    else:
        fla=6-(cor)
    
    pontos[l[0][0]]=cor
    pontos[l[0][1]]=fla
    
    return pontos