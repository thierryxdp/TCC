def primo(num):
    '''Função que retorna se um número é primo ou não.
    num=int->bool'''
    y=range(2,num)
    for n in y:
        if num % n==0:
            return False
    return True