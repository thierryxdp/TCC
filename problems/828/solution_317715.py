def primo(numero):
    '''funcao que verifica se um número é primo;
    int -> bool'''
    if numero > 1:
        for i in range(2,numero):
            if numero % i == 0:
                return True
        else:
            False