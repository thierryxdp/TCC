def primo(numero):
    """Função que indica se o número de entrada inteiro
    e positivo é primo ou não e retorna um valor booleano"""
    divisores = 0
    for divisor in list(range(2,numero+1)):
        sobra = numero%divisor
        if sobra ==0 and divisor!=numero:
            return Tru
    return False