def primo(num):
    '''função que averigua aprimalidade de um número
    int -> boolean value'''
    div = list(range(1, num+1))
    k = 0
    for i in div:
        if num%i != 0:
            k += 1
    if k == 2:
        return True
    else:
        return False