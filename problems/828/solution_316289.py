def qtd_divisores(numero):
    '''dado um numero inteiro, a funçao nos devolve o 
    numero de divisores inteiros desse numero
    int-->int'''
    soma=0
    for i in range(numero):
        if numero%(i+1)==0:
            soma=soma+1
    return soma

def primo(numero):
    '''dado um numero qualquer essa funçao nos devolve em forma
    de experçao booleana se o numero é prio (true) ou nao (false)
    int-->bool.'''
    if qtd_divisores(numero) == 2:
        return True
    else:
        return False