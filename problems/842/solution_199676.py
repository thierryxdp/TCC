def pontos_por_time(lista):
    '''a função deverá retornar um dicionário com os nomes dos times
    e seus pontos'''
      
    l1 = lista[0]
    l2 = lista[1]
   
    lista = [l1, l2]
    
    x = l1[2]
    y = l2[2]
    
    if x[0] > x[1] and y[1] > y[0]:
        return {l2[0]: 0, l2[1]: 6}
    elif x[0] < x[1] and y[1] < y[0]:
        return {l2[0]: 6, l2[1]: 0}
    elif x[0] == x[1] and y[0] == y[1]:
        return {l2[0]: 2, l2[1]: 2}
    elif x[0] > x[1] and y[1] < y[0]:
        return {l2[0]: 3, l2[1]: 3}
    elif x[0] < x[1] and y[1] > y[0]:
        return {l2[0]: 3, l2[1]: 3}
    elif x[0] > x[1] and y[0] == y[1]:
        return {l2[0]: 1, l2[1]: 4}
    elif x[1] > x[0] and y[0] == y[1]:
        return {l2[0]: 4, l2[1]: 1}
    elif x[0] == x[1] and y[1] > y[0]:
        return {l2[0]: 1, l2[1]: 4}
    elif x[0] == x[1] and y[0] > y[1]:
        return {l2[0]: 4, l2[1]: 1}