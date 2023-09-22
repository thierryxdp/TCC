def primo(numero):
    '''verifica se o número inserido é primo ou não; int -> bool'''

    cont = 0
    
    for i in range(1,numero+1):
        if numero%i == 0:
            cont = cont + 1
    if cont > 2:
        return False
    else:
        return True