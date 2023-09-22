def uppCons(frase):
    '''retorna a frase de entrada com suas vogais minusculas e as consoantes maiusculas
    str->str'''
    i=0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            maiuscula=str.upper(frase[i])
            substituir=str.replace(frase,frase[i],maiuscula)
            frase= substituir
        i=i+1
    return frase