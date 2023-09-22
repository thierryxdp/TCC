def filtra_pares(num1,num2,num3,num4):
    pares=()
    if num1%2==0:
        pares = pares + num1
    elif num2%2==0:
        pares = pares + num2
    elif num3%2==0:
        pares = pares + num3
    elif num4%2==0:
        pares = pares + num4
    else:
        return pares