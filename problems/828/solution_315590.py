def primo(num):
    """retorna a quantidade de divisores de um numero
    int -> int"""
    divisores = 0
    valor
    for numero in range(2,num):
        if num % numero == 0:
            divisores += 1
    if divisores == 0:
        valor = True
    else:
        valor = False
         
    return valor