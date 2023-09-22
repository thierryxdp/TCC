def primo(n):
    '''verifica se o numero dado é primo; int->str'''
    for divisor in range(2, n):
        if n % divisor == 0:
            return 'False'
    return 'True'