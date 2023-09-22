def primo(numero):
    """Funcao que dado um numero inteiro e positivo retorna se esse
    numero é primo
    int --> bool"""
    divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            divisores = divisores + 1
        if divisores != 0:
            primo = False
            return primo
        else:
            primo = True
    return primo