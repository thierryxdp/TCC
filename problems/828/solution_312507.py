def primo(n):
    'Funcao que dado um numero inteiro positivo, verifique se este numero é primo ou nao'
    for x in range(2,n):
        if n % x ==0:
            return False
    else:
            return True