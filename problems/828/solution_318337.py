def primo(n):
    '''Função que dado um numero inteiro positivo, verifica se o numero é primo ou nao
    int -> int'''
    x = 0
    for elem in range(1, n+1):
        if n%elem==0:
            x = x+1
	if x==2:
        return True
    else:
        return False