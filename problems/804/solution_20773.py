#Start your python function here

def filtra_pares(elementos):
    num1=int(elementos[0])
    num2=int(elementos[1])
    num3=int(elementos[2])
    num4=int(elementos[3])
    pares=[]
    if (num1%2==0):
        pares.append(num1)
    if (num2%2==0):
        pares.append(num2)
    if (num2%2==0):
        pares.append(num3)
    if (num4%2==0):
        pares.append(num4)
      
    elementospares = tuple(pares)
    return elementospares