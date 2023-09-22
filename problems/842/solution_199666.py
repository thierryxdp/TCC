def pontos_por_time(l):
    '''Função que, dada uma lista (l) de dois elementos, onde cada elemento também é uma lista, 
    retorna um dicionário contendo o nome do time e o número total de pontos na fase'''
    '''list -> dict'''
    sl1 = l[0]#sublista 1
    sl2 = l[1]#sublista 2
   
    lista = [sl1, sl2]
    
    a = sl1[2]
    b = sl2[2]
    
    if a[0] > a[1] and b[1] > b[0]:
        return {sl2[0]: 0, sl2[1]: 6}
    elif a[0] < a[1] and b[1] < b[0]:
        return {sl2[0]: 6, sl2[1]: 0}
    elif a[0] == a[1] and b[0] == b[1]:
        return {sl2[0]: 2, sl2[1]: 2}
    elif a[0] > a[1] and b[1] < b[0]:
        return {sl2[0]: 3, sl2[1]: 3}
    elif a[0] < a[1] and b[1] > b[0]:
        return {sl2[0]: 3, sl2[1]: 3}
    elif a[0] > a[1] and b[0] == b[1]:
        return {sl2[0]: 1, sl2[1]: 4}
    elif a[1] >  a[0] and b[0] == b[1]:
        return {sl2[0]: 4, sl2[1]: 1}
    elif a[0] == a[1] and b[1] > b[0]:
        return {sl2[0]: 1, sl2[1]: 4}
    elif a[0] == a[1] and b[0] > b[1]:
        return {sl2[0]: 4, sl2[1]: 1}