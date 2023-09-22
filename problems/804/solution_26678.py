#Start your pythondef par(y):
    return y%2 ==0
    '''função que recebe uma tupla com 4 números inteiros,
    e retorna apenas os pares. Caso não haja nenhum número par,
    retorna uma tupla vazia.
    assinatura: int,int,int,int > int,int,int,int
    casos de teste: filtra_pares([3,5,15,7]) ==()
    filtra_pares([24,10,-3,7]) ==(24, 10)
    filtra_pares([4,4,4,4]) ==(4, 4, 4, 4)'''
def filtra_pares(x):
    p = ()
    if par(x[0]):
        p = p + (x[0],)
    if par(x[1]):
        p = p + (x[1],)
    if par(x[2]):
        p = p + (x[2],)
    if par(x[3]):
        p = p + (x[3],)
    return p



def pontos(x):
    gols1= x[0]
    gols2= x[1]
    if gols1>gols2:
        return [3,0]
    if gols1<gols2:
        return [0,3]
    if gols1==gols2:
        return [1,1]
def pontos_por_time(x):
    jg1 = x[0]
    jg2 = x[1]
    t1 = jg1[0]
    t2 = jg1[1]
    gols1jg1 = jg1[2][0]
    gols2jg1 = jg1[2][1]
    gols1jg2 = jg2[2][0]
    gols2jg2 = jg2[2][1]
    pontosjg1 = pontos([gols1jg1 , gols2jg1])
    pontosjg2 = pontos([gols1jg2 , gols2jg2])
    pontost1= pontosjg1[0] + pontosjg2[1]
    pontost2= pontosjg1[1] + pontosjg2[0]
    return {t2:pontost2, t1:pontost1}