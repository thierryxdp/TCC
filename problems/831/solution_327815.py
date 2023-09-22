def lingua_p(palavra):
    ''' funcao que recebe uma palavra e traduz a palavra para
    a lingua do P
    str -> str'''
    vogais = 'aeiou'
    formato = palavra.lower()
    retorna = []
    for i in formato:
        if i in vogais:
            retorna.extend([i,'p',i])
        else:
            retorna.append(i)
     return str.join(' ',ret)