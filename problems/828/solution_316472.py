def primo(numero):
    """Função que recebe um número, e verifica se mesmo é primo ou não, e retorna um valor booleano
    int -> bool"""
    for i in range(2, numero // 2 + 1):
        if numero % i == 0:
            return False
    return True