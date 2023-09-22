def primo(n):
    ''' função que recebe um numero inteiro positivo, 
    verifica se este é primo ou não e retorna um
    valor booleano
    int --> bool'''
    num_primos = 0 
    for i in range (1, n+1):
        if n % i == 0:
           num_primos += 1
    if num_primos == 2: 
        return True
    else: 
        return False