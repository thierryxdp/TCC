def primo(n):
    '''funcao q dado um numero inteiro positivo, verifica se o
    numero eh primo, e retorna um valor booleano, caso seja primo eh True,
    senao eh False''' 
     cont = 0 
    for i in range(1, n+1):
        if n % i == 0:
            cont = cont + 1
    if i == 2:
        return True
    else:
        return False