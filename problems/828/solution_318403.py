def primo(n):
    """funcao que dado um n inteiro positivo, verifica se ele é primo ou nao, e retorna um valor bool;
    int->bool"""
    numerosPrimos=0
    for i in range(1, n + 1):
        if n % i == 0:
            numerosPrimos+=1
    if numerosPrimos==2:
        return true
    else:
        return false