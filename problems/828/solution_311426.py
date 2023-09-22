def primo(n):
    '''função que verifica se um número (n) dado é primo ou não;
    int -> bool'''
    p = True
    for i in range(2,n):
        if n%i == 0:
            p = False
    return p