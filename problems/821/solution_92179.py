def fatorial(numero):
    multiplicacao = 1
    for i in range(1, (numero+1)):
        multiplicacao *= i  
    return multiplicacao