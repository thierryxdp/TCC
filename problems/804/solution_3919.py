#Start your python function here
def filtra_pares(tupla):
    num1, num2, num3, num4 = tupla
    tuplaPar = 0
    if num1%2==0:
        tuplaPar + num1
        if num2%2==0:
            tuplaPar += num2
            if num3%2==0:
                tuplaPar += num3
                if num4%2==0:
                    tuplaPar += num4
                    return tuplaPar