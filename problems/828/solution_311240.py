def primo(numero):
    '''retorna a quantidade de divisores de um número, int->int'''
    soma=0
    for i in range(numero+1):
        if i!=0 and numero%i==0:
            soma=soma+1
    if soma==2:
        return True
    else:
        return False