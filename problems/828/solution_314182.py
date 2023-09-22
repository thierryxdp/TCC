def primo(n):
    ''' Função que verifica se um numero é primo ou não, ou seja, mostrar True se o numero só for divisivel por um e por ele mesmo.
int -> bool'''
    teste=0
    for i in range(2,n):
        if n % i == 0:
            teste = teste + 1
        if teste == 0:
            return True
        else:
            return False
    if n == 2:
        return True
    if n == 1:
        return False