def primo(numero):
    ''' Função que dado um número inteiro positivo, retorna
    True se ele for primo e False, caso contrário.
    Entrada: int
    Retorno: bool '''

    primos = []
    for x in range(2,numero+1):
        cont = 0

        for y in range(1,x+1):
            if x%y == 0:
                cont += 1
        if cont <= 2:
            list.append(primos,x)
    return numero in primos