def primo(inteiro):
    """Função que dado um número inteiro positivo, verifica
    se este é um número primo ou não e retorna um valor
    booleano;
    int -> bool"""
    divisores = 0
    for num in range(1, inteiro+1):
        if inteiro%num == 0:
            divisores = divisores + 1
    if divisores > 2:
            return False
    elif divisores <= 2:
            return True