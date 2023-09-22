def divisores(num):
    resultado=0
    for i in range(1, num//2+1):
        if num % i == 0: 
             resultado = resultado + 1
    return resultado