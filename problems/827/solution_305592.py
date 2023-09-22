def qtd_divisores(num):
    resultado=1
    for i in range(1, num//2+1):
        if num % i == 0: 
             resultado = resultado + 1
    return resultado