def pontos_por_time(x):
    if x[0][2][0]>x[0][2][1]:
        a=3 and k=0
    if x[0][2][0]==x[0][2][1]:
        a=1 and k=1
    else:
        a=0 and k=3
    if x[1][2][1]>x[1][2][0]:
        b=3 and f=0
    if x[1][2][1]==x[1][2][0]:
        b=1 and f=1
    else:
        b=0 and f=3
    d={x[0][0]:a+b ,x[0][1]:k+f }