def pontos_por_time(Lista):
    dic={}
    if Lista[0][2][0]>Lista[0][2][1]:
        dic[(Lista[0][0])]=3
        dic[(Lista[0][1])]=0
    elif Lista[0][2][0]==Lista[0][2][1]:
        dic[(Lista[0][0])]=1
        dic[(Lista[0][1])]=1
    if Lista[1][2][0]>Lista[1][2][1]:
        dic[(Lista[1][0])]=dic[(Lista[1][0])]+3
    elif Lista[1][2][0]==Lista[1][2][1]:
        dic[(Lista[1][0])]=dic[(Lista[1][0])]+1
        dic[(Lista[1][1])]=dic[(Lista[1][1])]+1
    return dic