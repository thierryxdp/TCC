def primo(n):
    '''verifica se o número é primo
    int -> bool'''
    lista = list(range(1,n+1))
    soma = 0
    for numero in lista:
        if n % numero == 0:
            soma = soma+1
    if soma == 2:
        return True
	if soma != 2:
        return False