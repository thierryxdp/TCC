import math
def qtd_divisores(numero):
    
    limite = math.ceil(numero**1/2)
    divisores = 0
    for i in range(1, limite):
        if numero % i == 0:
            divisores += 2
            print(i)
            
            if numero/i == i:
                divisores -= 1
    return divisores