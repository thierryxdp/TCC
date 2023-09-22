def primo(n):
    """funcao que verifica se um n° inteiro positivo, é primo ou mao, retornando o valor booleno;
    int->bool"""
    numerosPrimos = 0
    for i in range(1, n + 1):
         if n % i == 0:
            numerosPrimos += 1
    if numerosPrimos == 2:
        return True
    else:
        return false