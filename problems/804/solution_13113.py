def filtra_pares(tupla):
    '''Funcao recebe uma tupla contendo quatro elementos e retorna uma tupla contendo apenas os elementos pares
tupla -> tupla'''
    num1, num2, num3, num4 = tupla
    n1 = num1%2
    n2 = num2%2
    n3 = num3%2
    n4 = num4%2
    if (n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0):
        return num1, num2, num3, num4
    elif (n1 != 0 and n2 ==0 and n3 == 0 and n4 == 0):
        return num2, num3, num4
    elif(n1 == 0 and n2 !=0 and n3 != 0 and n4 != 0):
        return num1
    elif(n1 == 0 and n2 ==0 and n3 != 0 and n4 != 0):
        return num1, num2
    elif(n1 == 0 and n2 !=0 and n3 == 0 and n4 != 0):
        return num1, num3
    elif(n1 == 0 and n2 !=0 and n3 == 0 and n4 == 0):
        return num1, num4
    elif(n1 != 0 and n2 == 0 and n3 != 0 and n4 != 0):
        return num2
    elif(n1 != 0 and n2 ==0 and n3 == 0 and n4 != 0):
        return num2, num3
    elif(n1 != 0 and n2 ==0 and n3 != 0 and n4 == 0):
        return num2, num4
    elif(n1 != 0 and n2 !=0 and n3 == 0 and n4 == 0):
        return num3, num4
    elif(n1 != 0 and n2 !=0 and n3 != 0 and n4 == 0):
        return num4
    else:
        return