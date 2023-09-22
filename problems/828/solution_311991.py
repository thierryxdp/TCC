def primo(numero):
    '''Retorna se o numero dado é primo ou nao;
       Entrada: int;
       Saida: bool;
    '''
    for x in range(2, numero):
        if x == 2:
            return False
        if numero%x == 0:
            return False
        else:
            return True