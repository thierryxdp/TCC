def primo(numero):
    '''Funcao recebe um numero e verifica se ele e primo ou nao
int -> bool'''
    if(qtd_divisores(numero) == 2):
        return True
    else:
        return False