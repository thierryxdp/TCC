def primo(inteiro):
    '''
    função que dado um número inteiro positivo retorna se ele é primo ou não, por um booleano;
    int -> bool
    '''
    for num in range(2,inteiro):
        if inteiro%num != 0:
            return True
        else:
            return False