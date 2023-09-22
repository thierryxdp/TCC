def primo(numero):
    """Determinar um valor booleano, caso um numero inteiro e positivo seja primo;
    int -> bool"""
    i = 1
    soma = 0
    while  i <= numero:
        if numero % i == 0:
            soma += 1
        i = i+1
    if soma == 2:
        return True
    else:
        return False