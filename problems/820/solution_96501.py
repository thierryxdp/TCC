def ultima_vogal(palavra):
    '''retorna a ultima vogal da palavra
    str->str'''
    i=0
    vogal=''
    while i<len(palavra):
        if palavra[i] in 'AEIOUaeiou':
            vogal=palavra[i]
        i=i+1
    return vogal