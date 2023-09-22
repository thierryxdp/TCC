def qtd_divisores(numero):
    """retorna a quantidade de divisores que o numero tem;
    int->int"""
    divisores=0
    for n in range(1,numero+1):
        if numero/n in range(numero+1):
            divisores+=1
    return divisores
def primo(numero):
    """diz se um numero é primo ou não;
    int->bool"""
    if qtd_divisores(numero)==2:
        return True
    else:
        return False