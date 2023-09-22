def primo(n):
    '''funçao que dada um numero inteiro positivo analisa se o mesmo é primo ou não; int -> bool'''
    n_primo = 0
    for i in range (1, 1 + n):
        if n % 1 ==0:
            n_primo += 1
           
    if n_primo == 2:
        return True
    else:
        return False