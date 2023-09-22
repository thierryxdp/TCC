def primo(numero):
    '''funcao que verifica se um número é primo ou não;
    int -> bool'''
    divisores = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            divisores = divisores + 1
        if divisores > 1:
            return False 
    return True