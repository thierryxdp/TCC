def primo(numero):
    '''funcao que retorna se um numero e primo ou nao
    int->bool'''
    f=range(2, numero)
    for n in f:
        if numero % n ==0:
             return False
    return True