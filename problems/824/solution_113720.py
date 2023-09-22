def uppCons(frase):
    '''retorna a ultima vogal da palavra
    str->str'''
    i=0
    vogal=''
    while i<len(frase):
        if frase[i] != 'AEIOUaeiou' and '.' and '!':
            vogal=frase[i]
        i=i+1
    return vogal