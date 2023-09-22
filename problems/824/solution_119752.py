def uppCons(frase):
    '''funçao que recebe como entrada uma frase e retorna
    a frase com todas as consoantes maiusculas e os demais
    caracteres como estavam originalmente; str->str'''
    i=0
    nf='
    while i<len(frase):
        if frase[i]in'bcdfghjklmnpqrstvwxyz':
            nf+=str.upper(frase[i])
        else:
            nf+=frase[i]
        i=i+1
        return nf