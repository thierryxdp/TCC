def primo(x):
    """função que dado um numero inteiro positivo,verifica se esse numero é primo ou não; int->bool"""
    cont = 0
    for i in range(1, x+1):
        if x % i == 0:
            cont = cont + 1
    if cont == 2:
        return True
    else:
        return False