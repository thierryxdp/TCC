def primo(n):
    'Funcao que dado um numero inteiro positivo, verifique se este numero é primo ou nao'
    if n<=1:
        return False
    elif n==2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
        return True