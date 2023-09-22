#Start your python function here
'''A função pontos_por_time recebe uma lista contendo duas listas, que 
entregam o nome de dois times, e o placar de um jogo de ida e de volta.
Com isso, as funções auxiliares calculam ao final do processo o total de
pontos obtidos por cada time com base no placar dos jogos fornecidos 
pela lista x. Então, a função retorna um dicionário contendo o nome do 
time 1 e os pontos obtidos ao final dos dois jogos, e o mesmo para o time
2'''
def pt1j1(r1):
    gt1j1=(r1[0])
    gt2j1=(r1[1])
    if (gt1j1)>(gt2j1):
        return 3
    elif (gt1j1)==(gt2j1):
        return 1
    else:
        return 0
def pt1j2(r2):
    gt1j2=(r2[0])
    gt2j2=(r2[1])
    if (gt1j2)<(gt2j2):
        return 3
    elif (gt1j2)==(gt2j2):
        return 1
    else:
        return 0
def pft1(r1,r2):
    return ((pt1j1(r1))+(pt1j2(r2)))

def pt2j1(r1):
    gt2j1=(r1[1])
    gt1j1=(r1[0])
    if (gt2j1)>(gt1j1):
        return 3
    elif (gt2j1)==(gt1j1):
        return 1
    else:
        return 0
    
def pt2j2(r2):
    gt2j2=(r2[1])
    gt1j2=(r2[0])
    if (gt2j2)<(gt1j2):
        return 3
    elif (gt2j2)==(gt1j2):
        return 1
    else:
        return 0
    
def pft2(r1,r2):
    return ((pt2j1(r1))+(pt2j2(r2)))
    



def pontos_por_time(x):
    x1=x[0]
    y=x[1]
    t1=x1[0]
    t2=y[0]
    r1=x1[2]
    r2=y[2]
    gt1j1=r1[0]
    gt1j2=r2[0]
    gt2j1=r1[1]
    gt2j2=r2[1]
    

    
    
    
    
    
    

    return {str(t1):int(pft1(r1,r2)),
            str(t2):int(pft2(r1,r2))}