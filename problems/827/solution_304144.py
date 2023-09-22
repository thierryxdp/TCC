import math
def qtd_divisores(n):
    '''retorna o números de divisores do inteiro n'''
    if n<0:
        return 0
    '''obs*: discordo que o resultado esperado para números negativos seja 0'''
    qtd=2
    for i in range(2,math.ceil(n/2)+1):
        if n%i==0:
            qtd+=1
    return qtd