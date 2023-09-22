def pontos_por_time(l1):
    '''                       0 1                           0 1
    [['cormengo', 'flamengo',[1,0]], ['flamengo,'cormengo',[2,2]]
            0             1     2        0          1         2 
       (              0            ) (               1           )'''
    dicio1={str(l1[0][0]): 6, str(l1[0][1]): 0}
    dicio2={str(l1[0][1]): 6, str(l1[0][0]): 0}
    if l1[0][2][0] > l1[1][2][0]:
        return dicio1
    elif l1[0][2][1] > l1[1][2][1]:
        return dicio2