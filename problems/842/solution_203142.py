def pontos_por_time(lista):
    """diz quantos pontos no final da fase tem cada time, dada uma lista contendo os seguintes dados, no seguinte formato:
    [['nome do time 1', nome do time 2, [gols do time 1, gols do time 2]], ['nome do time 2', 'nome do time'[gols do time 2, gols do time 1]]]
    list -> dictionary"""
    p1 = 0
    p2 = 0
    nome1 = lista[0][0]
    nome2 = lista[0][1]
    if lista[0][2][0]>lista[0][2][1]:
        p1 = p1+3
    if lista[0][2][0]<lista[0][2][1]:
        p2 = p2+3
    if lista[0][2][0]==lista[0][2][1]:
        p1 = p1+1
        p2 = p2+1
    if lista[1][2][0]<lista[1][2][1]:
        p1 = p1+3
    if lista[1][2][0]>lista[1][2][1]:
        p2 = p2+3
    if lista[1][2][0]==lista[1][2][1]:
        p1 = p1+1
        p2 = p2+1
    return {nome1:p1 , nome2:p2}