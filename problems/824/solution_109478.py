def uppCons(frase):
    ''' Função que recebe uma frase e retorna a mesma frase com todas as suas consoantes em maiúsculas; str->str'''
    c=0
    f=''
    while c<len(frase):
        crc=frase[c]
        if str.lower(crc) in 'bcdfghjkçlmnpqrstvwxyz':
            crc = str.upper(crc)
        f=f+crc
        c=c+1
    return f