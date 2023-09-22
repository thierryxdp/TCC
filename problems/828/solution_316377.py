def qtd_divisores(num):
    """dado um numero, retorna quantos divisores este numero tem.
    int --> int"""
    divisores = 0
    for x in range(1,num+1):
        if num%x ==0:
            divisores = divisores + 1
    return divisores

def primo(num):
    """retorna true se o numero for primo e false caso nao seja,
    dado um numero interito positivo.
    int -> bool"""
    if qtd_divisores(num) == 2:
        return True
    else:
        return False