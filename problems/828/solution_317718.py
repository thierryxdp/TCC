def primo(numero):
    '''funcao que verifica se um número é primo;
    int -> bool'''
    if numero > 1:
        for count in range(2,numero):
            if numero % count == 0:
                return True
            else:
                 False