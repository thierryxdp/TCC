def uppCons(frase):
    '''
    dada uma frase retorne ela no entanto com os consoantes maiusculos
    entrada:string
    saida:string
    '''
    Cons = ''
    while caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            Cons += caractere.upper() 
        else: 
            Cons += caractere
    return Cons