def primo(n):
    '''Uma função dado um inteiro retornar se é primo ou não
    int -> booleano'''
d = 2
while d < n and primo:
        if n % d == 0:
            primo = False
        d += 1
    if primo and n != 1: # 1 não é primo
        print True
    else:
        print False