#Entrada: Um numero inteiro n
#1 - Para calcular o valor de H precisamos somar os numero 
#1.1 - de 1 até 1/n, na forma, 1+1/2+1/3...+1/n
#retornar essa soma
def soma_h(n:int)->float:
    """Recebe um número n e retorna 
    a soma de 1/1 ate 1/n, ou seja,
    1/1+1/2+1/3...+1/n"""
    for i int range(1, n+1):
        H+=H+1/i
   	return round(H,2)