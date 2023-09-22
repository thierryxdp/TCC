#Start your python function here
def filtra_pares(x):
    '''recebe uma tupla com 4 elementos inteiros e filtra apenas os pares, em ordem crescente
       tuple->tuple'''
    x1=x[0]
    x2=x[1]
    x3=x[2]
    x4=x[3]
    t = ()
    if (x1//2)==round(x1/2):
        t=t+(x1,)
    if (x2//2)==round(x2/2):
        t=t+(x2,)
    if (x3//2)==round(x2/2):
        t=t+(x3,)
    if (x4//2)==round(x4/2):
        t=t+(x4,)
    return t