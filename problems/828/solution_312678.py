def primo (n) :
    """Funcao que retorna um dado booleano de um numero inteiro indicando se ele e um numero primo ou não"""
    cont = 0
    i = 0

    while i <= n or cont < 2:
        i = i + 1
        x = n % i
        if x == 0:
            cont = cont + 1
            return False
        if cont <= 2:
            return True
        else :
            return False