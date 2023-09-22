def primo(numero):
    """Função que, dado um número inteiro positivo,
    verifica se este número é primo ou não. Retorna
    um valor booleano.
    int -> bool"""
    divisores = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            divisores = divisores + 1
    if divisores > 1:
        return False
    else return True