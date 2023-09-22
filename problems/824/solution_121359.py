def uppCons(frase):
    '''Recebe como entrada uma frase e retorna a frase com todas as suas
consoantes em maiúsculas e os demais caracteres exatamente como estavam na
frase original.'''
    i = 0
    cons = ['bcdfghjklmnpqrstvxwyz']
    frase2 = ''
    while i < len(frase):
        if frase[i] in cons:
            frase2 += frase[i].upper
        
        i = i+1

    return frase2