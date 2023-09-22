def qtd_divisores(numero):   
    soma=0
    for x in range(1,numero+1):
        if numero/x == int(numero/x):
            soma=1+soma

    return soma

def primo(numero):
    if qtd_divisores(numero)==2:
        return True
    return False