def fatorial(numero):
    '''
    Função que recebe um número e calcula o fatorial
    desse número.
    
    
    int -> int
    
    '''
    fat = 1
    c = 0
    while c < numero:
        c = c + 1
        fat = fat * c
    return fat