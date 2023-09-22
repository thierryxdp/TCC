def primo(n):
    '''Função que dado um numero inteiro,verifica se ele e primo.
    int->bool'''
    soma=0
    for c in range(1,n+1):
        if n%c==0:
        soma=soma+1
    if soma==2:
        return True
    else:
        return False