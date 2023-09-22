def pontos_por_time(v):
    """função que recebe uma lista de dois elementos com informações de dois times e recebe um dicionario com pontos na fase de acordo com os nomes do times"""
    if v[0][2][0]>v[0][2][1]:
        t1=3
        t2=0
    elif v[0][2][0]<v[0][2][1]:
        t1=0
        t2=3
    else:
        t1=1
        t2=1
    if v[1][2][0]>v[1][2][1]:
        t1=t1+0
        t2=t2+3
    elif v[1][2][0]<v[1][2][1]:
        t1=t1+3
        t2=t2+0
    else:
        t1=t1+1
        t2=t2+1
    return {v[0][0]:t1, v[0][1]:t2}ur python function here