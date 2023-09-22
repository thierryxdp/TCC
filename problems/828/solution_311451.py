def primo(num):
    """recebe um numero e retorna se esse e primo ou nao e primo """
    divisores = 0
    i = 1
    while i <= num:
        if num % i == 0 :
            divisores = divisores + 1
        i = i + 1

    if divisores == 2:
        return True
    else:
        return False