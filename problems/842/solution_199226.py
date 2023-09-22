def pontos_por_time(l1):
    '''                       0 1                           0 1
    [['cormengo', 'flamengo',[1,0]], ['flamengo,'cormengo',[2,2]]
            0             1     2        0          1         2 
       (              0            ) (               1           )'''
    dicio={str(l1[0][1]): 6, str(l1[0][0]): 0}
    if l1[0][2][0] and l1[1][2][1] > l1[0][2][1] or l1[1][2][0]:
        return dicio