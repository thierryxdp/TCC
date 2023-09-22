#Start your python function here
def pontos_por_time(A):
    '''recebe uma lista de dois elementos e retorna um dicionário com os times e os pontos que fizeram
       list -> dict'''
    B={}
    time1=A[[0][0]]
    time2=A[[0][1]]
    P1=0
    P2=0
    if A([[0][2][0]])>(A[[0][2][1]]):
        P1=3
    elif A([[0][2][0]])<(A[[0][2][1]]):
        P2=3
    else:
        P1=1
        P2=1
    if A([[1][2][0]])>(A[[1][2][1]]):
        P2=P2+3
    elif A([[1][2][0]])<(A[[1][2][1]]):
        P1=P1+3
    else:
        P1=P1+1
        P2=P2+1
    B={time1:P1, time2:P2}
    return B