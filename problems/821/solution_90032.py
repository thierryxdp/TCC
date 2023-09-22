def fatorial(num):
#Funcao que calcula o fatorial sem usar o modulo math
    n=num-1
    resultado=num
    while n>0:
        resultado=resultado*n
        n=n-1
    return resultado