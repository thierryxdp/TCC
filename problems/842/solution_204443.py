def pontos_por_time(lista):
    """list -> dict"""
    """recebe uma matriz(lista com listas) e retorna um dicionário com os pontos por time"""
    
    t1 = lista[0][0]
    t2 = lista[0][1]
    
    Pt1 = 0
    Pt2 = 0
    
    if lista[0][2][0] > lista[0][2][1]:
        Pt1 += 3
        Pt2 += 0
        pass
    
    elif lista[0][2][0] < lista[0][2][1]:
        Pt1 += 0
        Pt2 += 3
        pass
    
    else:
        Pt1 += 1
        Pt2 += 1
        pass
    
    if lista[1][2][0] < lista[1][2][1]:
        Pt1 += 3
        Pt2 += 0
        pass

    elif lista[1][2][0] > lista[1][2][1]:
        Pt1 += 0
        Pt2 += 3
        pass

    else:
        Pt1 += 1
        Pt2 += 1