def uppCons(frase):
    '''funçao que recebe uma frase de entrada e retorna todas
    as consoantes maiusculas e com os demais caracteres exatamente
    como estavam na frase original; str->str'''
    i=0
    nf=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            str.upper(frase)
        i=i+1
        return frase