def primo(num):
    """retorna se um numero é primo ou não
    int -> boolean"""
    divisores = 0
    valor = False
    for numero in range(2,num):
        if num % numero == 0:
            divisores += 1
    if divisores == 0:
        valor = True       
    return valor