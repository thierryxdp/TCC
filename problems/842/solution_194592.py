def pontos_por_time(lista_com_duas):
    '''Retorna um dicionario contendo os pontos que os times fizeram;
    lista,lista -> dicionário'''
    pontosA = 0
    pontosB = 0
    pontosFinal = {lista_com_duas[0[0]]:pontosA, lista_com_duas[0[1]]:pontosB}
    if lista_com_duas[0[3[0]]] > lista_com_duas[0[3[1]]]:
        pontosA += 3
    elif lista_com_duas[0[3[0]]] < lista_com_duas[0[3[1]]]:
        pontosB += 3
    elif lista_com_duas[0[3[0]]] == lista_com_duas[0[3[1]]]:
        pontosA += 1
        pontosB += 1
    if lista_com_duas[1[3[0]]] > lista_com_duas[1[3[1]]]:
        pontosB += 3
    elif lista_com_duas[1[3[0]]] < lista_com_duas[1[3[1]]]:
        pontosA += 3
    elif lista_com_duas[1[3[0]]] == lista_com_duas[1[3[1]]]:
        pontosA += 1
        pontosB += 1
    return pontosFinal