def filtra_pares(num1,num2,num3,num4):
    """Recebe uma tupla com quatro elementos num1,num2,num3 e num4 e retorna uma nova tupla somente
       com os elementos pares da tupla original
       parâmetros de entrada:int
       parâmetros de saída:int"""
    if num%2==0:
        return True
    else:
        return False
    nova_tupla=filter(filtra_pares(num1,num2,num3,num4))
    return nova_tupla