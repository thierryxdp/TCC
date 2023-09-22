def primo(n):
    '''Dado um número inteiro positivo, verifica se ele é primo.
int->bool'''
    divisores=()
    for x in range(1,n+1):
        if n%x==0:
            divisores+=(x,)
    if len(divisores)<=2:
        return True
    else:
        return False