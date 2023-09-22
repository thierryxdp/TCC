def uppCons(frase):
    '''Função que dada como entrada uma frase, retorne a 
    mesma frase com todas as consoantes em maiúsculas
    string --> string.'''
    x=0
    frase=0
    consoante='bcdfghjklmnpqrstvwxyz'
while x <len(frase):
    if frase[x] in consoante:
        frase = frase + 1
        x= x+1
        return (frase[x].upper).join