def qtd_divisores(numero):
    """ conta quantos divisores um numero tem e retorna
    int -> int"""
    i = 1
    divisores = 1
    while i < numero :
        if numero%i == 0 :
            divisores = divisores + 1
            i = i + 1
        else:
            i = i + 1
    return divisores