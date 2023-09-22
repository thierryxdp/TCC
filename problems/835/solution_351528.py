def melhor_volta(m):
    '''Dada uma matriz 6x10 com os tempos dos corredores em cada volta.
    Retorna de quem foi a melhor volta, com qual tempo e em qual volta.
    list->tuple'''
    a=[]
    i=0
    for lista in m:
        list.append(a,min(m[i]))
        i=i+1
    x=min(a)
    y=list.index(a,x)
    z=list.index(m[y],x)
    
    return ((y+1),x,(z+1))