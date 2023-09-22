'''teste2'''
def pontos1(x):
    if x[0][2][0]>x[0][2][1]:
        return 3
    elif x[0][2][0]==x[0][2][1]:
        return 1
def pontos2(x):
	if x[1][2][1]>x[1][2][0]:
        return 3
    elif x[1][2][1]==x[1][2][0]:
        return 1
def pontos3(x):
    if x[0][2][0]==x[0][2][1]:
        return 1
    elif x[0][2][0]<x[0][2][1]:
        return 3
    else:
        return 0
def pontos4(x):
    if x[1][2][1]==x[1][2][0]:
        return 1
    if x[1][2][1]<x[1][2][0]:
        return 3
    else:
        return 0
def pontos_por_time(x):
    time1=x[0][0]
    time2=x[0][1]
    dic={time1:pontos1(x)+pontos2(x) ,time2:pontos3(x)+pontos4(x)}
    return dic