def uppCons(frase):
    '''
    dada uma frase retorne ela no entanto com os consoantes maiusculos
    entrada:string
    saida:string
    '''
    Cons = ''
    i=0
    while i in frase:
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            Cons = frase[i].upper() 
        else: 
            Cons += frase[i]
    return Cons