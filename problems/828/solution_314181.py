def primo(numero):
    """Função que dado um número inteiro positivo, retorna 'True' caso este
    número seja um número primo ou 'False' caso contrário; int -> bool """

    primos = list()

    for num in range(1,numero+1):
        if (numero % num)== 0:
            list.extend(primos,[num])
    if len(primos) == 2:
        return True

    return False