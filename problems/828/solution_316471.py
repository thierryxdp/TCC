def primo(numero):
    '''Função que recebe um núemro inteiro positivo e retorna se ele é primo ou não
    int -> bool'''
    for i in range(2, numero // 2 + 1):
        if numero % i == 0:
            return False
    return True