def primo(n):
    ''' funcao que determina se uma numero eh primo ou nao
    int->bool'''
    soma = 0
    for i in range(2, n):
        if n % i == 0 :
            soma = soma + 1
    if soma == 0:
        return True
    else:
        return False