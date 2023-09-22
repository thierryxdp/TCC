#Start your python function here
def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

def filtra_pares(num1,num2,num3,num4):

    lista = num1,num2,num3,num4

    return list(filter(par,lista))