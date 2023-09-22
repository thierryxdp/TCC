def pontos_por_time(l1):
    '''recebe uma lista de dois elementos, sendo cada 
    elemento uma lista também.'''
    i1 = l1[0]
    i2 = l1[1]
    dic = {}
    pt1 = 0
    pt2 = 0
    if i1[2] > i1[3]:
        pt1 = pt1 + 3
    elif i1[2] == i1[3]:
        pt1 = pt1 + 1
        pt2 = pt2 + 1
    else:
        pt2 = pt2 + 3
        
    if i2[2] > i2[3]:
        pt1 = pt1 + 3
    elif i2[2] == i2[3]:
        pt1 = pt1 + 1
        pt2 = pt2 + 1
    else:
        pt2 = pt2 + 3
        
    dic = {i1[0] : pt1, i1[1]:pt2}
    return dic