def primo(numero):
    """A função recebe um numero inteiro positivo, e verifica se este 
    numero é primo ou não, retornando True caso seja ou False, caso não;
    int -> bool"""
    soma = 0 
    for i in range(1,numero+1):
        if numero%i == 0:
            soma += 1
    if soma == 2:
        return True
    else:
        return False