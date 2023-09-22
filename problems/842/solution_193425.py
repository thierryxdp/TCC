def pontos_por_time(lista):
    '''função que retorna um dicioário cujos mapeamentos são:<nome dotime> -> <numero total de pontos na fase'''
    a=lista[0][2][0]
    b=lista[0][2][1]
    c=lista[1][2][0]
    d=lista[1][2][1]
    nome1=lista[0][0]
    nome2=lista[0][1]
    time1=int()
    time2=int()
    
    if a>b:
        time1=3
    elif a==b:
        time1=1
        time2=1
    elif b>a:
        time2=3
    if d>c:
        time1=time1+3
    elif d==c:
        time1=time1+1
        time2=time2+1
    elif c>d:
        time2=time2+3
    
    if time1>time2:
        return {nome1:time1,nome2:time2}
    if time2>time1:
        return {nome2:time2,nome1:time1}