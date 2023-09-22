def primo(n):
    """dado um numero inteiro positivo, função verifica se esse numero é
    primo ou não. Primo = True, Não primo = False. int -> bool."""
    c = 2
    while n % c != 0 and c <= n/2:
        c = c + 1
    if n % c == 0:
        return False
    else:
        return True