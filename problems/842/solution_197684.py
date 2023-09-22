def pontos_por_time(lista):
    lista1 = lista[0]
    lista2 = lista1[2]
    lista3 = lista[1]
    lista4 = lista3[2]
    
    if lista2[0] > lista2[1] and lista4[1] > lista4[0]:
        return {lista1[0]:6, lista1[1]:0}
    elif lista2[0] > lista2[1] and lista4[1] == lista4[0]:
        return {lista1[0]:4, lista1[1]:1}
    elif lista2[0] > lista2[1] and lista4[1] < lista4[0]:
        return {lista1[0]:3, lista1[1]:3}
    elif lista2[0] == lista2[1] and lista4[1] > lista4[0]:
        return {lista1[0]:4, lista1[1]:1}
    elif lista2[0] == lista2[1] and lista4[1] == lista4[0]:
        return {lista1[0]:2, lista1[1]:2}
    elif lista2[0] == lista2[1] and lista4[1] < lista4[0]:
        return {lista1[0]:1, lista1[1]:4}
    elif lista2[0] < lista2[1] and lista4[1] > lista4[0]:
        return {lista1[0]:3, lista1[1]:3}
    elif lista2[0] < lista2[1] and lista4[1] == lista4[0]:
        return {lista1[0]:1, lista1[1]:4}
    elif lista2[0] < lista2[1] and lista4[1] < lista4[0]:
        return {lista1[0]:0, lista1[1]:6}