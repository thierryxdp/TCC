def primo(num):
    """Função que recebe um número e retorna um valor
    boleano para se o número é primo ou não
    int -> bool """
    d = 0
    for q in range(1, num + 1):
        if num%q == 0:
            d = d + 1
    if d == 2:
        return True
    else:
        return False