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