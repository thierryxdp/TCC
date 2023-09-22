def pontos_por_time(lista):
    '''Docs.
    list, list -> dict '''
    
    lista = [l1, l2]
    l1 = lista[0]
    l1 = l1[0:2]
    l2 = lista[1]
    l2 = l2[0:2]
    l1 = l1 + a
    l2 = l2 + b

#Gols que os times marcaram
	a = [[c, d]]
    b = [[e, f]]
    
    if a[0] > a[1] and b[1] > b[0]:
        return {str(l2[0]): 0, str(l2[1]): 6}
    elif a[1] > a[0] and b[0] > b[1]:
        return {str(l2[0]): 6, str(l2[1]): 0}
    elif a[0] == a[1] and b[0] == b[1]:
        return {str(l2[0]): 2, str(l2[1]): 2}
    elif a[0] > a[1] and b[1] < b[0]:
        return {str(l2[0]): 3, str(l2[1]): 3}
    elif a[1] > a[0] and b[1] > b[0]:
        return {str(l2[0]): 3, str(l2[1]): 3}
    elif a[0] > a[1] and b[0] == b[1]:
        return {str(l2[0]): 1, str(l2[1]): 4}
    elif a[0] < a[1] and b[0] == b[1]:
        return {str(l2[0]): 4, str(l2[1]): 1}
    elif a[0] == a[1] and b[1] > b[0]:
        return {str(l2[0]): 1, str(l2[1]): 4}
    elif a[1] == a[0] and b[0] > b[1]:
        return {str(l2[0]): 4, str(l2[1]): 1}