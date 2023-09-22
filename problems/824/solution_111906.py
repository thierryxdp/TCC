def uppCons(frase):
    '''função que recebe como entrada uma frase e retorna a frase com todas as suas consoantes maiusculas:str->str'''
    n = ''
    caractere = 0
    while caractere<len(frase):
        if frase[caractere] in 'bcdfghjklmnpqrstvwxyzç':
            n+= frase[caractere].upper()
        else:
            n += frase[caractere] 
        caractere += 1
    return n