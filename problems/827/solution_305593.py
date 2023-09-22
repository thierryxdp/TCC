def qtd_divisores(num):
    resultado=1
    for i in list(range(1, num)):
        if num % i == 0: 
             resultado = resultado + 1
    return resultado