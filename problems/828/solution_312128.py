def primo(n):
    '''Função que dado um numero positivo, verifica se é um numero primo ou não.
    int -> bool'''
    p = 1
    for i in range (1, n//2+1):
        if n % i == 0:
            p += 1
        elif p>2:
            return False
        if p == 2:
            return True
        else:
            return False