def primo(numero):
    ''' Função que dado um número inteiro positivo, retorna
    True se ele for primo e False, caso contrário.
    Entrada: int
    Retorno: bool '''

    for x in range(2,numero):
        if numero % x == 0:
            return False
    return True