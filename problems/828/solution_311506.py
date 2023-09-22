def primo(n):
    """Dado um número 'n' inteiro e positivo, a função verifica se o número
    é primo ou não. Caso seja primo retorna True, caso o contrário retorna
    False;
    int -> boolean"""
    divisores = []

    for x in range(2,n):
        if n%x == 0:
            list.append(divisores,x)
    div = len(divisores)
    return div == 0