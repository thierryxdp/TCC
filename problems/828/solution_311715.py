def primo(n):
    '''funcao que dado um numero verifica se ele é primo
int -> int'''
    assert (type(n) is int) and (n >=0)
    metade = n//2
    divisor = 2
    _primo = True
    while (divisor <= metade) and (_primo):
        _primo = ((n% divisor)!=0)
        divisor = divisor + 1
    return _primo