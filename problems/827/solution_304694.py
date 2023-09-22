def qtd_divisores (n) :
    """Funcao que retorna quantos divisores um numero de entrada tem"""
    i = 0
    acum = 0
    while i <= n // 2 :
        if  n%i == 0 :
            acum = acum + 1
    i = i + 1
    return acum