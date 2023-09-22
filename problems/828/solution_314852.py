def primo(num):
    """Funcao que recebe um numero inteiro positivo "num" de entrada
   e verifica se este numero é primo, retornando um valor booleano "True"
   caso seja primo ou "False" caso não seja"""
    """ int -> bool"""
    divisores = 0
    for a in range(1, num + 1):
        if num % a == 0:
            divisores += 1
    if divisores == 2:
        return True
    else:
        return False
    #Casos de teste
    """ primo(15)
    >>> False
        primo(2)
    >>> True
        primo(13)
    >>> True """