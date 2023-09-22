def pontos_por_time(lista):
    if lista[0][2][0] > lista[0][2][1]:
        pontoscor1 == '3' and pontosfla1 == '0'
    if lista[0][2][0] == lista[0][2][1]:
        pontoscor1 == '1' and pontosfla1 == '1'
    if lista[0][2][0] < lista[0][2][1]:
        pontoscor1 == '0' and pontosfla1 == '3'
    if lista[1][2][0] < lista[1][2][1]:
        pontoscor2 == ']' and pontosfla2 == '0'
    if lista[1][2][0] == lista[1][2][1]:
        pontoscor2 == ']' and pontosfla2 == '1'
    if lista[0][2][0] > lista[0][2][1]:
        pontoscor2 == '0' and pontosfla2 == '3'
    pontoscor = int(pontoscor1) + int(pontoscor2)
    pontosfla = int(pontosfla1) + int(pontosfla2)
    pontosportime = {'Cormengo': pontoscor, 'Flamínthians': pontosfla}
    return pontosportime
        #Start your python function here