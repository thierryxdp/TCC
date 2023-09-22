def fatorial(n: int) -> int:
    """ recebe um número inteiro e calcula o fatorial deste número """

    i = 1
    fatorial = 1
    
    while i < n+1:
        
        fatorial = fatorial * i

        i = i + 1
        
    return fatorial