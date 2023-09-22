#Start your python function here
def filtra_pares(a,b,c,d):
    """função que recebe uma tupla com quatro numeros inteiros e retorne uma nova tupla que tem elementos pares respectivamente; tuple,tuple,tuple,tuple-> int"""
    if (a%2==0):
        return a
    elif (b%2==0):
        return b
    elif (c%2==0):
        return c
    elif (d%2==0):
        return d
    else:
        return a,b,c,d