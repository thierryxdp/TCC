def pontos_por_time(l1): 
    '''recebe uma lista de dois elementos, sendo cada 
    elemento uma lista também.'''
    i1 = l1[0]
    p1 = i1[2]
    i2 = l1[1]
    p2 = i2[2]
    dic = {}
    pt1 = 0
    pt2 = 0
    if p1[0] > p1[1]:
        pt1 = pt1 + 3
    elif p1[0] == p1[1]:
        pt1 = pt1 + 1
        pt2 = pt2 + 1
    else:
        pt2 = pt2 + 3
        
    if p2[0] > p2[1]:
        pt1 = pt1 + 3
    elif p2[0] == p2[1]:
        pt1 = pt1 + 1
        pt2 = pt2 + 1
    else:
        pt2 = pt2 + 3
        
    dic = {i1[0] : pt1, i1[1]:pt2}
    return dic