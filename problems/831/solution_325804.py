def lingua_p(palavra):
    '''funcao que ao receber uma palavra traduz a palavra
para língua do P
str -> str'''
    vogais = 'aeiou'
    f = palavra.lower()
    ret =[]
    for i in f:
        if i in vogais:
            ret.extend([i,'p',i])
        else:
            ret.append(i)
    return str.join('',ret)