def pontos_por_time(lista):
    '''Função retorna dicionário com nome dos times em determinada fase; list->dict'''
    if lista[0][2][0]==lista[0][2][1]:
        a=1
        b=1
    if lista[0][2][0]>lista[0][2][1]:
        a=3
        b=0
    if lista[0][2][0]<lista[0][2][1]:
        a=0
        b=3
    if lista[1][2][0]==lista[1][2][1]:
        c=1
        d=1
    if lista[1][2][0]>lista[1][2][1]:
        c=3
        d=0
    if lista [1][2][0]<lista[1][2][1]:
        c=0
        d=3
    dic={lista[0][0]:(a),lista[0][1]:b)}
    dic2={lista[1][0]:(b+c),lista[1][1]:(a+d)}
    return dic2