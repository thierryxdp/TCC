def uppCons(frase):
    '''retorna frase com apenas consoantes e maiusculas'''
    i=0
    Texto=''
    while i<len(frase):
        if frase[i] in 'bcçdfghklmnpqrstjvwxyz':
            
            Texto=Texto+str.upper(frase[i])
        else: Texto=Texto+frase[i]
        i=i+1
    return Texto