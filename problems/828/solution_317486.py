def primo(inteiro):
    '''
    função que dado um número inteiro positivo retorna se ele é primo ou não, por um booleano;
    int -> bool
    '''
    qtd_divisores = 0
    for num in range(1,inteiro+1):
        if inteiro%num == 0:
            qtd_divisores = qtd_divisores + 1
    if qtd_divisores > 2:
        return False
    elif qtd_divisores <= 2:
        return True