'''teste2'''
def pontos1(x):
    if x[0][2][0]>x[0][2][1]:
        return 3
    elif x[0][2][0]==x[0][2][1]:
        return 1
def pontos2(x):
	if x[1][2][1]>x[1][2][0]:
        return 3
    elif x[1][2][1]<x[1][2][0]:
        return 1
def pontos_por_time(x):
    time1=x[0][0]
    time2=x[0][1]
    dic={time1:pontos1+pontos2 ,time2:0}
    return dic