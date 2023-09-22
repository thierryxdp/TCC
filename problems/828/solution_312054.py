def primo(numero):
    '''Retorna se o numero dado é primo ou nao;
       Entrada: int;
       Saida: bool;
    '''
    contador = 0
    for x in range(1, numero+1):
        if x == 2:
            return True
        if numero%x == 0:
            contador = contador +1
                return False
        else:
            return True