#Start your python function here
def pontos_por_time(lista):
    lista1 = lista[0]
    lista2 = lista[1]
    lista = [lista1 + lista2]
    lista3 = lista1[2]
    lista4 = lista2[2]
    if lista3[0] > lista3[1] and lista4[0] < lista4[1]:
        return {lista1[0]:6, lista1[1]:0}
    elif lista3[0] > lista3[1] and lista4[0] > lista4[1]:
        return {lista1[0]:3, lista1[1]:3}
    elif (lista3[0] > lista3[1] and lista4[0] == lista4[1]) or (lista3[0] == lista3[1] and lista4[0] < lista4[1]):
        return {lista1[0]:4, lista1[1]:1}
    elif lista3[0] < lista3[1] and lista4[0] < lista4[1]:
        return {lista1[0]:3, lista1[1]:3}
    elif lista3[0] < lista3[1] and lista4[0] > lista4[1]:
        return {lista1[0]:0, lista1[1]:6}
    elif (lista3[0] == lista3[1] and lista4[0] > lista4[1]) or (lista3[0] < lista3[1] and lista4[0] == lista4[1]):
        return {lista1[0]:1, lista1[1]:4}
    else:
        return {lista1[0]:2, lista1[1]:2}