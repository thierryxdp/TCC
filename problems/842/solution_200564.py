lista1=[t1i,t2i,[gols1i,gols2i]]
lista2=[t2v,t1v,[gols2v,gols1v]]        
def pontos_por_time ([lista1],[lista2]):
    ''' .'''
    nome_t1= t1i
    nome_t2= t2i
    if gols1i == gols2i:
        i1=1
        i2=2
    elif gols1i > gols2i:
        i1=4
    elif gols1i < gols2i:
        i2=4
    else:
        i1=0
        i2=0
        
    if gols1v == gols2v:
        v1=1
        v2=1
    elif gols1v > gols2v:
        v1=4
    elif gols1v < gols2v:
        v2=4
    else :
        v1=0
        v2=0
        
    total_p1=i1+v1
    total_p2=i2+v2
    
    return {nome_t1: total_p1, nome_t2: total_p2}