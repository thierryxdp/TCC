def primo(numero):
    """Funcao recebe um numero e retrona True se o numero for primo ou False caso contrario
    int -> bool"""
    divisores = []
    for i in range(1,numero+1):
        if numero%i == 0:
            divisores.append(i)
    if len(divisores) <= 2:
        return True
    else: 
        return False