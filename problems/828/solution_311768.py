def primo(num):
    '''
        Função que retorna se o número passado é primo.
        Int => Int
    ''' 
    p = True
    if (num == 4):
        p = False
    else:
        for i in range(2, num//2):
            if (num % i == 0):
                p = False
                break
    return p