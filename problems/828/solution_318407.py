def primo(n):
    '''Função que dado um nº inteiro positivo, retorna se este nº é primo
ou não.
int -> bool'''
    primos = 0
    for num in range(1, n + 1):
        if n % num == 0:
            primos += 1
    if primos == 2:
        return True
    else:
        return False