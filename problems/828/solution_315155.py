def primo(num):
    '''funcao que verifica se um numero é primo ou não; int -> bool'''
    divisores = 0
    for divisor in range(1, num+1):
        if num % divisor == 0:
            divisores = divisores + 1
    if divisores == 2:
        return True
    else:
        return False