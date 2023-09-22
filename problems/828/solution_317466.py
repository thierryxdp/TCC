def primo(num):
    """Função recebe um inteiro positivo e verifica se é primo ou não,
       retornando um valor booleano. 
       int -> bool
    """
    c = 0
    for x in range(1, num+1):
        if num % x == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False