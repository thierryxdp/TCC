tupla=(int,int,int,int)
def filtra_pares(tupla):
    num1=tupla[0]
    num2=tupla[1]
    num3=tupla[2]
    num4=tupla[3]
    
    if num4%2==0 and num1%2!=0 and num2%2!=0 and num3%2!=0:
        return (num4)

     elif num1%2==0 and num4%2!=0 and num2%2!=0 and num3%2!=0:
        return (num1)
    elif num2%2==0 and num4%2!=0 and num1%2!=0 and num3%2!=0:
        return (num2)
    elif num3%2==0 and num4%2!=0 and num2%2!=0 and num1%2!=0:
        return (num3)
    elif num1%2==0 and num4%2==0 and num2%2!=0 and num3%2!=0:
        return (num1,num4)
    elif num1%2==0 and num2%2==0 and num4%2!=0 and num3%2!=0:
        return (num1,num2)
    elif num1%2==0 and num3%2==0 and num2%2!=0 and num4%2!=0:
        return (num1,num3)
    elif num2%2==0 and num4%2==0 and num1%2!=0 and num3%2!=0:
        return (num2,num4)
    elif num3%2==0 and num4%2==0 and num2%2!=0 and num1%2!=0:
        return (num3,num4)
    elif num3%2==0 and num2%2==0 and num4%2!=0 and num1%2!=0:
        return (num2,num3)
    elif num1%2==0 and num4%2==0 and num2%2==0 and num3%2!=0:
        return (num1,num2,num4)
    elif num1%2==0 and num3%2==0 and num2%2==0 and num4%2!=0:
        return (num1,num2,num3)
    elif num1%2==0 and num4%2==0 and num3%2==0 and num2%2!=0:
        return (num1,num3,num4)
    elif num1%2==0 and num4%2==0 and num2%2==0 and num3%2!=0:
        return (num1,num2,num4)
    elif num3%2==0 and num4%2==0 and num2%2==0 and num1%2!=0:
        return (num2,num3,num4)
    elif num1%2==0 and num4%2==0 and num2%2==0 and num3%2!=0:
        return (num1,num2,num4)
    elif num1%2==0 and num4%2==0 and num2%2==0 and num3%2==0:
        return (num1,num2,num3,num4)