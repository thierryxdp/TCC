def filtra_pares(num1,num2,num3,num4):
    pares=()
    if num1%2==0:
        pares = pares + num1
    if num2%2==0:
        pares = pares + num2
    if num3%2==0:
        pares = pares + num3
    if num4%2==0:
        pares = pares + num4
    else:
        return pares