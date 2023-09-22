def qtd_divisores(num):
    contador = 0
    
    for numero in range(1, num+1):
        if num % numero == 0:
            contador +=1
    if numero < 0:
        return contador
    else:
        return contador