#Start your python function here
def filtra_pares(x):
    """A função recebe uma tupla com quatro elementos inteiros, e
    retorna outra tupla contendo apenas os elementos pares recebidos"""
    
    num = ()
    num1 = int(x[0])
    num2 = int(x[1])
    num3 = int(x[2])
    num4 = int(x[3])
    


    if num1%2 == 0:
        num= num + (num1,)
    
    if num2%2 == 0:
        num= num+ (num2,)
    
    if num3%2 == 0:
        num= num+ (num3,)
    
    if num4%2 == 0:
        num= num+ (num4,)
    return num