def pontos_por_time (resultado):
    '''retorna o total de pontos de dois times em uma fase'''
    'resultado[[nome1,nome2,[gols1,gols2]],[nome2,nome1[gols2,gols1]]]'
    p1=0
    p2=0
    if resultado[0][2][0]>resultado[0][2][1]:
        p1=p1+3
    elif resultado[0][2][0]<resultado[0][2][1]:
        p2=p2+3
    else:
        p1=p1+1
        p2=p2+1
    if resultado[1][2][0]>resultado[1][2][1]:
        p2=p2+3
    elif resultado[1][2][0]<resultado[1][2][1]:
        p1=p1+3
    else:
        p1=p1+1
        p2=p2+1
    return {resultado[0][0]:p1,resultado[0][1]:p2}