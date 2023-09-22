def filtra_pares(*n):
    num0 = n[0]
    num1 = n[1]
    num2 = n[2]
    num3 = n[3]
    par = ()

    if num0 % 2 ==0:
      par = par + (num0,)
    if num1 % 2 ==0:
      par = par + (num1,)
    if num2 % 2 ==0:
      par = par + (num2,)
    if num3 % 2 ==0:
      par = par + (num3,)

    print (par)