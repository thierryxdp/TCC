def primo(numero):
   	divisores = 0
    resultado = False
    for x in range(1, numero+1):
        if numero % x == 0:
            divisores += 1
        
    if divisores == 2:
        resultado = True
    else: 
        resultado = False
    return resultado