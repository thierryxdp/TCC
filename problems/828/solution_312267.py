def primo(numero):
    '''Funcao que retorna um valor booleano 
    dizendo True -> se o numero for primo e 
    False -> se o numero nao for primo.
    Dados de entrada: int
    Valor de saida: bool
    '''
    if numero <= 0:
        return False
    elif numero == 2:
        return True
    for n in range(2,numero):
        if numero % n == 0:
            return False
    return True