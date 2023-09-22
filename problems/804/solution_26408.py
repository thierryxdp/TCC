def par(a):
    if a%2==0:
        return True
    else:
        return False

r = ([])

def a(a):
    if par(a[0]) == True:
        return r + [a[0],]
    else:
        return ([])
def b(a):
    if par(a[1]) == True:
        return r + [a[1], ]
    else:
        return ([])
def c(a):
    if par(a[2]) == True:
        return r + [a[2],]
    else:
        return ([])
def d(a):
    if par(a[3]) == True:
        return r + [a[3],]
    else:
        return ([])
def filtra_pares(e):
    '''Esta função recebe uma quatro números inteiros, e retorna uma tupla somente com os
    números pares
    assinatura tuple -> tuple
    testes:
    filtra_pares([4,8,10,12])=(4,8,10,12)
    filtra_pares([1,3,5,7])=()
    filtra_pares([0,0,0,0])=(0,0,0,0)
    '''
    return tuple(a(e)+b(e)+c(e)+d(e))