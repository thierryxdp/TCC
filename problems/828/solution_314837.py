def primo(numero):
    '''função que recebe como entrada um numero inteiro positivo e retorna True
caso esse número seja primo, e False caso não seja; int->bool'''

    if numero<2:
        return False

    for x in range(2,numero):
        if numero%x==0:
            return False
    return True