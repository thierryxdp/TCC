def primo(numero):
    '''função que verifica se um número é primo ou não, retornando trua caso ele seja primo e false caso nao seja;int->bool'''
    for i in list(range(2,numero)):
        if numero%i==0:
            return bool(0)
    return bool(1)