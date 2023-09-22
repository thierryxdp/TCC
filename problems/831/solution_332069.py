def lingua_p(palavra):
    '''
    Funçao que recebe uma palavra e transforma ela na ligua do p
    str -> str
    '''
    a=''
    vogais=['a','e','i','o','u']
    for i in palavra:
        if i in vogais:
            a=a+i+'p'+i
        else:
            a=a+i
    return a