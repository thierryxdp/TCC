def resto(a, b):
    return a % b

def eh_par(n):
    return resto(n, 2) == 0

def filtra_pares(t):
    """Recebe uma tupla com quatro elementos inteiros
e retorna uma nova tupla com apenas os elementos que são pares
assinatura: tuple --> tuple
testes:
filtra_pares([100, 200, 300, 400]) == (100, 200, 300, 400)
filtra_pares([10, 25, 30, 60]) == (10, 30, 60)
filtra_pares([1, 2, 3, 4]) == (2, 4)
filtra_pares([5, 10, 15, 25]) == (10,)
filtra_pares([7, 17, 27, 37]) == ()
"""   
    ret = ()
    if eh_par(t[0], ):
        ret = ret + (t[0], )
    if eh_par(t[1], ):
        ret = ret + (t[1], )
    if eh_par(t[2], ):
        ret = ret + (t[2], )
    if eh_par(t[3], ):
        ret = ret + (t[3], )
    return ret