#Start your python function here
def filtra_pares(num1, num2, num3, num4):
    num1, num2, num3, num4 = tupla
    if num1%2!=0:
        tupla.remove(num1)
        if num2%2!=0:
            tupla.remove(num2)
            if num3%2!=0:
                tupla.remove(num3)
                if num4%2!=0:
                    tupla.remove(num4)
                    return tupla